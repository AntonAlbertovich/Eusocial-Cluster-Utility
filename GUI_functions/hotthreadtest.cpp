// CPP program to demonstrate multithreading 
// using three different callables. 
// By Anton Rakos
//This is a simple test which uses multithreading to test out the basic capabilites of a node within a cluster.
//This program should only cause a minor spike in waste heat production and CPU usage.
#include <iostream> 
#include <thread> 
#include <chrono>
#include <ctime>
#include <sys/time.h>
typedef std::chrono::high_resolution_clock Clock;
using namespace std; 
long fib_seq (long n) {
	long result;
	if (n < 2) {
		result = n;
		} 
	else {
		long X, Y;
		X = fib_seq(n-1);
		Y = fib_seq(n-2);
		result = X + Y;
  		}
	return result;
	}
void fib_seq_sleep_a(long int T, int X, int Y, int Z) { 

	for (int i = 0; i < X; i++) { 
		auto start = std::chrono::high_resolution_clock::now();
		long j = fib_seq(Y);
		struct timeval tp;
		gettimeofday(&tp, NULL);
		long int end_time = tp.tv_sec * 1000 + tp.tv_usec / 1000;
		std::cout <<"Done in: "; 
		auto finish = std::chrono::high_resolution_clock::now();
		std::cout << std::chrono::duration_cast<std::chrono::nanoseconds>(finish-start).count() << "ns ";
		cout << "Done at:" << end_time - T << "ms from start time ";
		std::cout << "A:Fib_seq:" << j << " Now holding for " << Z << " s \n"; 
		std::chrono::seconds hold_for(Z);
		std::this_thread::sleep_for(hold_for);

		} 
	}

void fib_seq_sleep_b(long int T, int X, int Y, int Z) { 

	for (int i = 0; i < X; i++) { 
		auto start = std::chrono::high_resolution_clock::now();
		long j = fib_seq(Y);
		struct timeval tp;
		gettimeofday(&tp, NULL);
		long int end_time = tp.tv_sec * 1000 + tp.tv_usec / 1000;
		std::cout <<"Done in: "; 
		auto finish = std::chrono::high_resolution_clock::now();
		std::cout << std::chrono::duration_cast<std::chrono::nanoseconds>(finish-start).count() << "ns ";
		cout << "Done at:" << end_time - T << "ms from start time ";
		std::cout << "B:Fib_seq:" << j << " Now holding for " << Z << " s \n"; 
		std::chrono::seconds hold_for(Z);
		std::this_thread::sleep_for(hold_for);

		} 
	}

void fib_seq_sleep_c(long int T, int X, int Y, int Z) { 

	for (int i = 0; i < X; i++) { 
		auto start = std::chrono::high_resolution_clock::now();
		long j = fib_seq(Y);
		struct timeval tp;
		gettimeofday(&tp, NULL);
		long int end_time = tp.tv_sec * 1000 + tp.tv_usec / 1000;
		std::cout <<"Done in: "; 
		auto finish = std::chrono::high_resolution_clock::now();
		std::cout << std::chrono::duration_cast<std::chrono::nanoseconds>(finish-start).count() << "ns ";
		cout << "Done at:" << end_time - T << "ms from start time ";
		std::cout << "C:Fib_seq:" << j << " Now holding for " << Z << " s \n"; 
		std::chrono::seconds hold_for(Z);
		std::this_thread::sleep_for(hold_for);

		} 
	}

void fib_seq_sleep_d(long int T, int X, int Y, int Z) { 

	for (int i = 0; i < X; i++) { 
		auto start = std::chrono::high_resolution_clock::now();
		long j = fib_seq(Y);
		struct timeval tp;
		gettimeofday(&tp, NULL);
		long int end_time = tp.tv_sec * 1000 + tp.tv_usec / 1000;
		std::cout <<"Done in: "; 
		auto finish = std::chrono::high_resolution_clock::now();
		std::cout << std::chrono::duration_cast<std::chrono::nanoseconds>(finish-start).count() << "ns ";
		cout << "Done at:" << end_time - T << "ms from start time ";
		std::cout << "D:Fib_seq:" << j << " Now holding for " << Z << " s \n"; 
		std::chrono::seconds hold_for(Z);
		std::this_thread::sleep_for(hold_for);

		} 
	}
int main() 
{
	struct timeval tp;
	gettimeofday(&tp, NULL);
	long int ms = tp.tv_sec * 1000 + tp.tv_usec / 1000;
	thread th0(fib_seq_sleep_a, ms, 1, 40, 0); 
	thread th1(fib_seq_sleep_b, ms, 1, 40, 0); 
	thread th2(fib_seq_sleep_c, ms, 1, 40, 0); 
	thread th3(fib_seq_sleep_d, ms, 1, 40, 0); 
	thread th4(fib_seq_sleep_a, ms, 1, 40, 0); 
	thread th5(fib_seq_sleep_b, ms, 1, 40, 0); 
	thread th6(fib_seq_sleep_c, ms, 1, 40, 0); 
	thread th7(fib_seq_sleep_d, ms, 1, 40, 0); 
	th0.join();
	th1.join();
	th2.join();
	th3.join();
	th4.join();
	th5.join();
	th6.join();
	th7.join();
	cout<<"-------------------------- Non-Threaded--------------------------\n" ;
	struct timeval tp1;
	gettimeofday(&tp1, NULL);
	long int ms1 = tp1.tv_sec * 1000 + tp1.tv_usec / 1000;
	fib_seq_sleep_a(ms1, 1, 40, 0); 
	fib_seq_sleep_b(ms1, 1, 40, 0); 
	fib_seq_sleep_c(ms1, 1, 40, 0); 
	fib_seq_sleep_d(ms1, 1, 40, 0); 
	fib_seq_sleep_a(ms1, 1, 40, 0); 
	fib_seq_sleep_b(ms1, 1, 40, 0); 
	fib_seq_sleep_c(ms1, 1, 40, 0); 
	fib_seq_sleep_d(ms1, 1, 40, 0); 
	return 0; 
} 
