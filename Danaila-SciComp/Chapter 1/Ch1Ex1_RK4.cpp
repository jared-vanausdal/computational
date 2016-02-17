/*
########################################################
##                                                    ##
##                   CH1EX1_RK4.CPP                   ##
##                                                    ##
########################################################


This file implements the fourth order Runge-Kutta scheme for solving ODEs of the first
order. Given the time interval and boundary points t0 and tn, the initial condition u0,
and the number of steps between t0 and tn.
*/

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

double RHS(double t, double u){
	return -4.0 * u;
}

vector<double> PDE_RK4(vector<double> &u, vector<double> &t, double u0, double t0, double tn, int n){

	double k1, k2, k3, k4;

	double h = (tn - t0)/n;
	
	u[0] = u0;	
	
	for(int i = 0; i < n; i++){
		k1 = h * RHS(t[i],u[i]);
		k2 = h * RHS(t[i]+(h/2),u[i]+(k1/2));
		k3 = h * RHS(t[i]+(h/2),u[i]+(k2/2));
		k4 = h * RHS(t[i]+h,u[i]+k3);
		u[i+1] = u[i] + (1.0/6)*(k1 + 2*k2 + 2*k3 + k4); 
	}
	
	return u;
}

int main(){
	ofstream output;
	output.open("RK4.csv");

	double t0 = 0.0, tn = 3.0;
	double h = 0.5;
	double u0 = 1.0;
	int n = 6;

	vector<double> u, t;

	u.resize(n);
	t.resize(n);
	
	// Initialize the T, and U vectors
	for (int i = 0; i <= n; i++){
		u[i] = 0;
		t[i] = 0 + i*h;
	}

	PDE_RK4(u,t,u0,t0,tn,n);

	output << "Time,U,Initial Time," << t0 << ",Final Time," << tn <<",Time Step," << h << endl;

	for (int i = 0; i <= n; i++){
		output << t[i] << "," << u[i] << endl;	
	}
	
	output.close();

	return 0;
}
