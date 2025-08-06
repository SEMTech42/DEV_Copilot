import * as React from 'react';
import { INewsItem } from '../models/INewsItem';

export interface ITopNewsProps {
  newsItems: INewsItem[];
  isLoading: boolean;
  hasError: boolean;
  errorMessage?: string;
}

export interface ITopNewsState {}