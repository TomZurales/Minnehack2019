import {Component, OnInit} from '@angular/core';
import {Observable} from 'rxjs';
import {Auction, RestService} from '../rest.service';

@Component({
  selector: 'app-auction',
  templateUrl: './auction.component.html',
  styleUrls: ['./auction.component.scss']
})
export class AuctionComponent implements OnInit {

  dataSource: Observable<Auction[]>;
  tableColumns: string[] = ['name', 'current_bid', 'highest_bidder', 'end_date', 'bid_button'];

  constructor(private restService: RestService) {
  }

  ngOnInit() {
    this.restService.getAuctions().subscribe((result) => {
      this.dataSource = result.auctions;
      console.log(this.dataSource);
    });
  }

}
