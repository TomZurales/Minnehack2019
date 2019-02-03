import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class RestService {
  REST_URL = 'http://35.192.186.196';

  constructor(private http: HttpClient) {
  }

  getTasks() {
    return this.http.get(this.REST_URL + '/tasks/tasks');
  }

  getTaskHistory(userID: number) {
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
