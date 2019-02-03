import {Component, OnInit} from '@angular/core';
import {RestService, Task} from '../rest.service';
import {Observable} from 'rxjs';

@Component({
  selector: 'app-tasks',
  templateUrl: './tasks.component.html',
  styleUrls: ['./tasks.component.scss']
})
export class TasksComponent implements OnInit {

  dataSource: Observable<Task[]>;
  tableColumns: string[] = ['name', 'value'];

  constructor(private restService: RestService) {
  }

  ngOnInit() {
    this.restService.getTasks().subscribe((result) => {
      this.dataSource = result.tasks;
    });
  }

}
