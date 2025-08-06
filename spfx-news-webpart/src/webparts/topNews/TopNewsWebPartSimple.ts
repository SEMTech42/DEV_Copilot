import { Version } from '@microsoft/sp-core-library';
import {
  IPropertyPaneConfiguration,
  PropertyPaneTextField,
  PropertyPaneSlider
} from '@microsoft/sp-property-pane';
import { BaseClientSideWebPart } from '@microsoft/sp-webpart-base';

import { ITopNewsWebPartProps } from './ITopNewsWebPartProps';

export default class TopNewsWebPart extends BaseClientSideWebPart<ITopNewsWebPartProps> {

  public render(): void {
    this.domElement.innerHTML = `
      <div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px;">
        <div style="font-size: 28px; font-weight: 600; color: #0078d4; margin-bottom: 24px; text-align: center; border-bottom: 2px solid #c7e0f4; padding-bottom: 12px;">
          ⭐ Top 5 Rated News
        </div>
        <div id="newsContainer" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-top: 20px;">
          <div style="text-align: center; padding: 40px 20px; font-size: 16px; background: rgba(0, 120, 212, 0.1); color: #0078d4; border: 1px solid #c7e0f4; border-radius: 8px;">
            Loading top rated news...
          </div>
        </div>
      </div>
    `;
    
    this.loadTopRatedNews();
  }

  private async loadTopRatedNews(): Promise<void> {
    const newsContainer = this.domElement.querySelector('#newsContainer');
    if (!newsContainer) return;

    try {
      const newsListTitle = this.properties.newsListTitle || 'Site Pages';
      const maxItems = this.properties.maxItems || 5;
      
      // Create sample news data for demonstration
      const sampleNews = [
        {
          Id: 1,
          Title: "SharePoint Framework Updates: Enhanced Performance and New Features",
          Description: "Microsoft announces major updates to SPFx with improved performance, new React hooks support, and enhanced development experience for SharePoint Online.",
          Created: new Date().toISOString(),
          AuthorName: "Microsoft SharePoint Team",
          BannerImageUrl: "https://via.placeholder.com/400x200/0078d4/ffffff?text=SharePoint+News",
          OriginalSourceUrl: "#",
          Rating: 5,
          FirstPublishedDate: new Date().toISOString()
        },
        {
          Id: 2,
          Title: "Microsoft 365 Security Enhancements: Zero Trust Architecture",
          Description: "New security features in Microsoft 365 implement Zero Trust principles, providing enhanced protection for corporate data and user identities.",
          Created: new Date(Date.now() - 86400000).toISOString(),
          AuthorName: "Microsoft Security Team",
          BannerImageUrl: "https://via.placeholder.com/400x200/107c10/ffffff?text=Security+News",
          OriginalSourceUrl: "#",
          Rating: 5,
          FirstPublishedDate: new Date(Date.now() - 86400000).toISOString()
        },
        {
          Id: 3,
          Title: "Teams Integration with SharePoint: Seamless Collaboration",
          Description: "Enhanced integration between Microsoft Teams and SharePoint enables seamless document collaboration and improved workflow automation.",
          Created: new Date(Date.now() - 172800000).toISOString(),
          AuthorName: "Microsoft Teams Team",
          BannerImageUrl: "https://via.placeholder.com/400x200/6264a7/ffffff?text=Teams+News",
          OriginalSourceUrl: "#",
          Rating: 5,
          FirstPublishedDate: new Date(Date.now() - 172800000).toISOString()
        },
        {
          Id: 4,
          Title: "Power Platform Integration: Low-Code Solutions for Everyone",
          Description: "New Power Platform integrations with SharePoint enable citizen developers to create powerful business applications without extensive coding.",
          Created: new Date(Date.now() - 259200000).toISOString(),
          AuthorName: "Microsoft Power Platform Team",
          BannerImageUrl: "https://via.placeholder.com/400x200/742774/ffffff?text=Power+Platform",
          OriginalSourceUrl: "#",
          Rating: 5,
          FirstPublishedDate: new Date(Date.now() - 259200000).toISOString()
        },
        {
          Id: 5,
          Title: "AI-Powered Content Discovery in SharePoint Online",
          Description: "Microsoft Copilot integration brings AI-powered content discovery and intelligent recommendations to SharePoint document libraries.",
          Created: new Date(Date.now() - 345600000).toISOString(),
          AuthorName: "Microsoft AI Team",
          BannerImageUrl: "https://via.placeholder.com/400x200/d83b01/ffffff?text=AI+News",
          OriginalSourceUrl: "#",
          Rating: 5,
          FirstPublishedDate: new Date(Date.now() - 345600000).toISOString()
        }
      ];

      const newsItemsHtml = sampleNews.slice(0, maxItems).map(item => `
        <div style="background: white; border-radius: 8px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); overflow: hidden; transition: transform 0.2s ease, box-shadow 0.2s ease; border: 1px solid #edebe9;">
          <div style="width: 100%; height: 180px; overflow: hidden;">
            <img src="${item.BannerImageUrl}" alt="${item.Title}" style="width: 100%; height: 100%; object-fit: cover;" />
          </div>
          <div style="padding: 16px;">
            <div style="margin-bottom: 12px;">
              <a href="${item.OriginalSourceUrl}" style="font-size: 18px; font-weight: 600; color: #0078d4; text-decoration: none; display: block; line-height: 1.3;">
                ${item.Title}
              </a>
            </div>
            <div style="display: flex; align-items: center; margin-bottom: 12px; gap: 8px;">
              <span style="font-size: 16px;">⭐⭐⭐⭐⭐</span>
              <span style="font-size: 12px; color: #0078d4; font-weight: 600; background: rgba(0, 120, 212, 0.1); padding: 2px 8px; border-radius: 12px;">5-Star Rating</span>
            </div>
            <div style="color: #605e5c; font-size: 14px; line-height: 1.4; margin-bottom: 12px; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden;">
              ${item.Description}
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; font-size: 12px; color: #a19f9d; border-top: 1px solid #edebe9; padding-top: 8px;">
              <span style="font-weight: 500;">By ${item.AuthorName}</span>
              <span style="font-style: italic;">${new Date(item.FirstPublishedDate).toLocaleDateString()}</span>
            </div>
          </div>
        </div>
      `).join('');

      newsContainer.innerHTML = newsItemsHtml;

    } catch (error) {
      console.error('Error loading news:', error);
      newsContainer.innerHTML = `
        <div style="text-align: center; padding: 40px 20px; font-size: 16px; background: rgba(164, 38, 44, 0.1); color: #a4262c; border: 1px solid rgba(164, 38, 44, 0.3); border-radius: 8px;">
          Error loading news: ${error.message || 'Unknown error occurred'}
        </div>
      `;
    }
  }

  protected get dataVersion(): Version {
    return Version.parse('1.0');
  }

  protected getPropertyPaneConfiguration(): IPropertyPaneConfiguration {
    return {
      pages: [
        {
          header: {
            description: 'Configure the Top 5 Rated News web part'
          },
          groups: [
            {
              groupName: 'Settings',
              groupFields: [
                PropertyPaneTextField('description', {
                  label: 'Description'
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