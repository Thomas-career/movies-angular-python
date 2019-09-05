import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { BehaviorSubject } from 'rxjs';
import { SharedService } from './shared/shared.service'

@Injectable({
  providedIn: 'root'
})
export class Service {
  isChannelCreated: Boolean = false;

  private dataSource = new BehaviorSubject('hi');
  data = this.dataSource.asObservable();

  constructor(
    private http: HttpClient,
    private sharedService: SharedService
  ) { }


  updatedDataSelection(hi) {
    this.dataSource.next(hi);
  }

  // post
  post(url, payload): Observable<any> {
    return this.http.post(this.sharedService.API_URL + url, payload);
  }

  // put
  put(url, payload): Observable<any> {
    return this.http.put(this.sharedService.API_URL + url, payload);
  }

  // get
  get(url): Observable<any> {
    return this.http.get(this.sharedService.API_URL + url);
  }

  // delete
  delete(url): Observable<any> {
    return this.http.delete(this.sharedService.API_URL + url);
  }

  setChannelTrue(value: boolean) {
    this.isChannelCreated = value;
  }
}
