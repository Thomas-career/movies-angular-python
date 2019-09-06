import { Component, OnInit } from '@angular/core';
import { SettingsService } from '../../../core/settings/settings.service';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { CustomValidators } from 'ng2-validation';
import { Router } from '@angular/router';
import { Constants } from '../../../config/Constant';
import { Service } from '../../../app.service';

import { UserblockService } from '../../../layout/sidebar/userblock/userblock.service';

@Component({
    selector: 'app-login',
    templateUrl: './login.component.html',
    styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

    valForm: FormGroup;
    responseMessage: String;
    userDetails:any;

    constructor(private service: Service, public userblockService: UserblockService,private router: Router,public settings: SettingsService, fb: FormBuilder) {

        this.valForm = fb.group({
            'email': [null, Validators.compose([Validators.required, CustomValidators.email])],
            'password': [null, Validators.required]
        });

    }

    submitForm($ev, value: any) {
        $ev.preventDefault();
        for (let c in this.valForm.controls) {
            this.valForm.controls[c].markAsTouched();
        }
        if (this.valForm.valid) {
            console.log('Valid!');

            const url = `${Constants.userLogin}`;
            this.service.post(url, value)
                .subscribe(data => {
                    this.userDetails=data;
                    localStorage.setItem('currentUser', JSON.stringify(data));
                    // this.userblockService.toggleVisibility();
                    this.router.navigate(['/movie/list'])
                }, error => {
                    console.error('error:', error);
                    if (error.error.unauthorized) { this.responseMessage = "failed"; }
                });
        }
    }

    ngOnInit() {

    }

}
