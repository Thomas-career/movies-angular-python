import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { SharedModule } from '../../shared/shared.module';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';


@NgModule({
    imports: [
        SharedModule,
        // RouterModule.forChild(routes)
    ],
    declarations: [
        LoginComponent,
        RegisterComponent
    ],
    exports: [
        RouterModule,
        LoginComponent,
        RegisterComponent
    ]
})
export class PagesModule { }
