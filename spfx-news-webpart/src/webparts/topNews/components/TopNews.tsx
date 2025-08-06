import * as React from 'react';
import { ITopNewsProps, ITopNewsState } from './ITopNewsProps';
import { INewsItem } from '../models/INewsItem';
import styles from './TopNews.module.scss';

export default class TopNews extends React.Component<ITopNewsProps, ITopNewsState> {

  public render(): React.ReactElement<ITopNewsProps> {
    const { newsItems, isLoading, hasError, errorMessage } = this.props;

    if (isLoading) {
      return (
        <div className={styles.topNews}>
          <div className={styles.container}>
            <div className={styles.row}>
              <div className={styles.column}>
                <div className={styles.loading}>Loading top rated news...</div>
              </div>
            </div>
          </div>
        </div>
      );
    }

    if (hasError) {
      return (
        <div className={styles.topNews}>
          <div className={styles.container}>
            <div className={styles.row}>
              <div className={styles.column}>
                <div className={styles.error}>
                  Error loading news: {errorMessage}
                </div>
              </div>
            </div>
          </div>
        </div>
      );
    }

    if (!newsItems || newsItems.length === 0) {
      return (
        <div className={styles.topNews}>
          <div className={styles.container}>
            <div className={styles.row}>
              <div className={styles.column}>
                <div className={styles.noNews}>No 5-star rated news items found.</div>
              </div>
            </div>
          </div>
        </div>
      );
    }

    return (
      <div className={styles.topNews}>
        <div className={styles.container}>
          <div className={styles.row}>
            <div className={styles.column}>
              <div className={styles.title}>
                ⭐ Top 5 Rated News
              </div>
              <div className={styles.newsGrid}>
                {newsItems.map((item: INewsItem) => (
                  <div key={item.Id} className={styles.newsCard}>
                    {item.BannerImageUrl && (
                      <div className={styles.newsImage}>
                        <img src={item.BannerImageUrl} alt={item.Title} />
                      </div>
                    )}
                    <div className={styles.newsContent}>
                      <div className={styles.newsTitle}>
                        <a href={item.OriginalSourceUrl} target="_blank" rel="noopener noreferrer">
                          {item.Title}
                        </a>
                      </div>
                      <div className={styles.newsRating}>
                        <span className={styles.stars}>⭐⭐⭐⭐⭐</span>
                        <span className={styles.ratingText}>5-Star Rating</span>
                      </div>
                      <div className={styles.newsDescription}>
                        {item.Description}
                      </div>
                      <div className={styles.newsMetadata}>
                        <span className={styles.author}>By {item.AuthorName}</span>
                        <span className={styles.date}>
                          {new Date(item.FirstPublishedDate || item.Created).toLocaleDateString()}
                        </span>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}