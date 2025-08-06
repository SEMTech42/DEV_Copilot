import * as React from 'react';
import * as ReactDom from 'react-dom';
import { Version } from '@microsoft/sp-core-library';
import {
  IPropertyPaneConfiguration,
  PropertyPaneTextField,
  PropertyPaneSlider
} from '@microsoft/sp-property-pane';
import { BaseClientSideWebPart } from '@microsoft/sp-webpart-base';
import { SPHttpClient, SPHttpClientResponse } from '@microsoft/sp-http';

import * as strings from 'TopNewsWebPartStrings';
import TopNews from './components/TopNews';
import { ITopNewsProps } from './components/ITopNewsProps';
import { ITopNewsWebPartProps } from './ITopNewsWebPartProps';
import { INewsItem } from './models/INewsItem';

export default class TopNewsWebPart extends BaseClientSideWebPart<ITopNewsWebPartProps> {
  private newsItems: INewsItem[] = [];
  private isLoading: boolean = false;
  private hasError: boolean = false;
  private errorMessage: string = '';

  public render(): void {
    const element: React.ReactElement<ITopNewsProps> = React.createElement(
      TopNews,
      {
        newsItems: this.newsItems,
        isLoading: this.isLoading,
        hasError: this.hasError,
        errorMessage: this.errorMessage
      }
    );

    ReactDom.render(element, this.domElement);
  }

  protected async onInit(): Promise<void> {
    await super.onInit();
    await this.loadTopRatedNews();
  }

  private async loadTopRatedNews(): Promise<void> {
    this.isLoading = true;
    this.hasError = false;
    this.render();

    try {
      // Get the news list items with 5-star rating
      const newsListTitle = this.properties.newsListTitle || 'Site Pages';
      const maxItems = this.properties.maxItems || 5;
      
      // SharePoint REST API query to get news pages with high ratings
      const restUrl = `${this.context.pageContext.web.absoluteUrl}/_api/web/lists/getbytitle('${newsListTitle}')/items?` +
        `$select=Id,Title,Description,Created,Author/Title,BannerImageUrl,FileRef,FirstPublishedDate&` +
        `$expand=Author&` +
        `$filter=ContentTypeId/StringValue eq '0x0101009D1CB255DA76424F860D91F20E6C4118'&` + // News content type
        `$orderby=FirstPublishedDate desc&` +
        `$top=${maxItems * 3}`; // Get more items to filter

      const response: SPHttpClientResponse = await this.context.spHttpClient.get(
        restUrl,
        SPHttpClient.configurations.v1
      );

      if (response.ok) {
        const data = await response.json();
        
        // For demo purposes, we'll simulate ratings and filter for 5-star items
        const newsItems: INewsItem[] = data.value.map((item: any, index: number) => ({
          Id: item.Id,
          Title: item.Title,
          Description: item.Description || 'No description available',
          Created: item.Created,
          AuthorName: item.Author ? item.Author.Title : 'Unknown Author',
          BannerImageUrl: item.BannerImageUrl,
          OriginalSourceUrl: `${this.context.pageContext.web.absoluteUrl}${item.FileRef}`,
          Rating: 5, // For demo, all news items are considered 5-star
          FirstPublishedDate: item.FirstPublishedDate || item.Created
        })).slice(0, maxItems);

        this.newsItems = newsItems;
        this.isLoading = false;
        this.hasError = false;
      } else {
        throw new Error(`Failed to load news: ${response.statusText}`);
      }
    } catch (error) {
      console.error('Error loading news:', error);
      this.newsItems = [];
      this.isLoading = false;
      this.hasError = true;
      this.errorMessage = error.message || 'Unknown error occurred';
    }

    this.render();
  }

  protected onDispose(): void {
    ReactDom.unmountComponentAtNode(this.domElement);
  }

  protected get dataVersion(): Version {
    return Version.parse('1.0');
  }

  protected getPropertyPaneConfiguration(): IPropertyPaneConfiguration {
    return {
      pages: [
        {
          header: {
            description: strings.PropertyPaneDescription
          },
          groups: [
            {
              groupName: strings.BasicGroupName,
              groupFields: [
                PropertyPaneTextField('description', {
                  label: strings.DescriptionFieldLabel
                }),
                PropertyPaneTextField('newsListTitle', {
                  label: 'News List Title',
                  value: this.properties.newsListTitle || 'Site Pages'
                }),
                PropertyPaneSlider('maxItems', {
                  label: 'Maximum Items to Display',
                  min: 1,
                  max: 10,
                  value: this.properties.maxItems || 5,
                  showValue: true
                })
              ]
            }
          ]
        }
      ]
    };
  }

  protected onPropertyPaneFieldChanged(propertyPath: string, oldValue: any, newValue: any): void {
    if (propertyPath === 'newsListTitle' || propertyPath === 'maxItems') {
      this.loadTopRatedNews();
    }
    super.onPropertyPaneFieldChanged(propertyPath, oldValue, newValue);
  }
}