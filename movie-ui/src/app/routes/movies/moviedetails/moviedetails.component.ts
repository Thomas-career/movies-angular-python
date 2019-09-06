import { Component, OnInit } from '@angular/core';
import { Movie } from '../movie';
import { Constants } from '../../../config/Constant';
import { Service } from '../../../app.service';
import { ActivatedRoute } from '@angular/router';
import 'rxjs/add/operator/filter';

@Component({
  selector: 'app-moviedetails',
  templateUrl: './moviedetails.component.html',
  styleUrls: ['./moviedetails.component.scss']
})
export class MoviedetailsComponent implements OnInit {

  constructor(private route: ActivatedRoute, private service: Service) { }

  movieDetails: Movie;

  ngOnInit() {
    this.route.queryParams
      .filter(params => params.id)
      .subscribe(params => {
        console.log(params);
        this.getMovieById(params.id);
      });
  }

  getMovieById(movie_id) {
    const url = `${Constants.getMoviesById}${movie_id}`;
    this.service.get(url)
      .subscribe(data => {
        this.movieDetails = data;
      }, error => {
        console.error('error:', error);
      });
  }

}
