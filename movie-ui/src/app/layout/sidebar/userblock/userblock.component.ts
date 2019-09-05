import { Component, OnInit } from '@angular/core';

import { UserblockService } from './userblock.service';

@Component({
    selector: 'app-userblock',
    templateUrl: './userblock.component.html',
    styleUrls: ['./userblock.component.scss']
})
export class UserblockComponent implements OnInit {
    user: any;
    constructor(public userblockService: UserblockService) {
        // this.user = {
        //     picture: 'assets/img/user/03.jpg'
        // };
    }


    ngOnInit() {
        this.getUserDetails()
    }

    userBlockIsVisible() {
        return this.userblockService.getVisibility();
    }

    getUserDetails() {
        this.user = JSON.parse(localStorage.getItem('currentUser'));
        if (this.user) {
            console.log("user------->",this.user);
            this.user.picture='assets/img/user/03.jpg' 
            this.userblockService.toggleVisibility(); 
        }
    }

}
