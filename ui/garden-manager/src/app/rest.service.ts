import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RestService {
  REST_URL = 'http://35.192.186.196';

  constructor(private http: HttpClient) {
  }

  getTasks(): Observable<any> {
    return this.http.get(this.REST_URL + '/tasks/tasks');
  }

  getTaskHistory(userID: number): Observable<any> {
    return this.http.get(this.REST_URL + '/tasks/history?id=' + userID);
  }
}


export class Task {
  value: number;
  name: string;
  interval: number;
  lastCompleted: Date;
  id: number;
}
