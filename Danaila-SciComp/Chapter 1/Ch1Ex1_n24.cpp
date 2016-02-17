/* 
########################################################
##                                                    ##
##                   CH1EX1_N24.CPP                   ##
##                                                    ##
########################################################


This file implements the explicit Euler scheme for solving ODEs of the first order.
Given the time interval and boundary points t0 and tn, the initial condition u0,
and the number of steps between t0 and tn.
*/

#define VERBOSE false

#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;


double RHS(double t, double u){
	return -4.0 * u;
}

vector<double> PDE_EulerExp(vector<double> &u, vector<double> &t, double u0, double t0, double tn, int n){
	u[0] = u0;
	if (VERBOSE){
		cout << "ENTERED PDE_EULEREXP" << endl;
	}	
	double h = (tn - t0) / n;
	
	if (VERBOSE){
		for(int i = 0; i <= t.size(); i++){
			cout << "t[" << i << "]: " << t[i] << " -- u[" << i << "]: " << u[i] << endl;
		}

		cout << "\n";	
	}

	for(int i = 0; i < n; i++){
		u[i+1] = u[i] + h * RHS(t[i],u[i]);
		if (VERBOSE){
			cout << "t[" << i << "]: " << t[i] << " u["<< i << "]: " << u[i] << endl;
		}
	}
	
	return u;
}

int main(){
	
	// Setting up file for output
	ofstream output; 
	output.open("ExpEuler_n24.csv");


	double t0 = 0.0, tn = 3.0;
	double h;
	int n = 24;
	double u0 = 1.0;

	vector<double> u, t;

	u.resize(n);
	t.resize(n);
	if (VERBOSE){
		cout << "Size of u: " << u.size() << " Size of t: " << t.size() << endl;
	}
	h = (tn-t0)/n;

	// Initialize both the u and t vectors
	for (int i = 0; i <= n; i++){
		u[i] = 0;
		t[i] = 0 + i*h;
	}
	
	if (VERBOSE){
		cout << "\nIN MAIN" << endl;

		for (int i = 0; i <= n; i++){
			cout << "t[" << i << "]: " << t[i] << " -- u[" << i << "]: " << u[i] << endl;	
		}

		cout << "\n";

		cout << "*** Parameters Passed to PDE_EulerExp ***" << endl;
		cout << "u0 = " << u0 << ", t0 = " << t0 << ", tn = " << tn << ", n = " << n << "\n" << endl;
	}

	PDE_EulerExp(u, t, u0, t0, tn, n);
	
	if (VERBOSE){	
		cout << "RETURNED TO MAIN" << endl;

		for(int i = 0; i <= n; i++){
			cout << "t[" << i << "]: " << t[i] << " u[" << i << "]: " << u[i] << endl;
		}

	}
	
    output << "Time,U,Initial time," << t0 << ",Final time," << tn << ",Time Step," << h << endl;
	
	for(int i = 0; i <= n; i++){
		output << t[i] << "," << u[i] << endl;
	}	

	output.close();
	

	if (VERBOSE){
		cout << "Time step size: " << h << endl;
		cout << "Size of Time vector: " << t.size() << endl;
		cout << "Size of U vector: " << u.size() << endl;
		cout << "t0 = " << t[0] << " tn = " << t[n] << endl;
	}
	return 0;
}
