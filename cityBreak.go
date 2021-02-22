// cityBreak.go

package main

import (
	"fmt"
	"reflect"
	)

type city struct {
	Flight  int; 
	Hotel int; 
	Car  int;
}
var pf, lf, rf, ph, lh, rh, pc, lc, rc int

func main(){
	// create the three city break costs
	Paris:= city{
		Flight: 200,
		Hotel: 20,
		Car: 200,
	}
	London:= city{
		Flight: 200,
		Hotel: 20,
		Car: 200,
	}
	Rome:= city{
		Flight: 200,
		Hotel: 20,
		Car: 200,
	}
// A bit of type assertion to change from {} to integers
	p_values := reflect.ValueOf(Paris)
	pvalues := make([]interface{}, p_values.NumField())
	
	// Workings to pull out the initial values for each cost for Paris break Flights *2, Hotel * 7, Car * 1
	for i := 0; i < p_values.NumField(); i++ {
		pvalues[i] = p_values.Field(i).Interface()
		if i == 0 {
			pf := pvalues[0].(int)
			pf = pf * 2 
			fmt.Println("Paris")
			fmt.Println(" Flights cost: ",pf)
			} else if i == 1 {
				ph := pvalues[1].(int)
				ph = ph * 7
				fmt.Println(" Hotel costs: ",ph)
				} else if i == 2{
					pc := pvalues[2].(int)
					fmt.Println(" Car Rental costs: ",pc)
				}
			}
			
			
// Workings to pull out the initial values for each cost for London break Flights *2, Hotel * 7, Car * 1
	l_values := reflect.ValueOf(London)
	lvalues := make([]interface{}, l_values.NumField())
	for i := 0; i < l_values.NumField(); i++ {
		lvalues[i] = l_values.Field(i).Interface()
		if i == 0 {
			lf := lvalues[0].(int)
			lf = lf * 2
			fmt.Println("London")
			fmt.Println(" Flights cost: ",lf)
			} else if i == 1 {
				lh := lvalues[1].(int)
				lh = lh * 7
				fmt.Println(" Hotel costs: ",lh)
				} else if i == 2{
					lc := lvalues[2].(int)
				fmt.Println(" Car Rental costs: ",lc)
			}
		}
		
// Workings to pull out the initial values for each cost for Rome break Flights *2, Hotel * 7, Car * 1
	r_values := reflect.ValueOf(Rome)
	rvalues := make([]interface{}, r_values.NumField())
		for i := 0; i < r_values.NumField(); i++ {
			rvalues[i] = r_values.Field(i).Interface()
			if i == 0 {
				rf := rvalues[0].(int)
				rf = rf * 2
			fmt.Println("Rome")
			fmt.Println(" Flights cost: ",rf)
			} else if i == 1 {
				rh := rvalues[1].(int)
			rh = rh * 7
			fmt.Println(" Hotel costs: ",rh)
		} else if i == 2{
			rc := rvalues[2].(int)
			fmt.Println(" Car Rental costs: ",rc)
		}
	}
}