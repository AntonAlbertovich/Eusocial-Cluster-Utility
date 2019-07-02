//Last edit 3/18/2018...   
//Compile with: g++ -o runthis_c NrPcPA.cpp 
//As part of ECU this is just a program which serves as an example of who ECU manages C++ programs
//This specific program serves no other funcion in the way in which ECU opperates.
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <string>
#include <cmath>
#include <sstream>
#include <cstdio>
#include <deque>
using namespace std;
typedef struct AST *pNODE;
struct AST {string info; pNODE children[2];};

//These are the structers which are specified in the outline Programming Project 1: Boolean Expression Ecvaluator 
struct tokRslt{
        bool success; //The first field of tokRslt
        vector<string> syms; //The Secound field of tokRslt
        };
struct parseRslt{
        bool success; //The first field of parseRslt
        AST ast;
        };
struct TPERslt{
        bool val;
        string msg;
        };


tokRslt tokenize(string s);

parseRslt parse(vector<string> V);


TPERslt TPE(string s);

string TPEOut(string s);

tokRslt tokenize(string s){
        int input_size = s.size();
        tokRslt out;
        for (int i = 0; i < input_size; i++){

                if (s[i] == 'T' || s[i] == 'F' || s[i] == '^' || s[i] == 'v' || s[i] == '~' || s[i] == '(' || s[i] == ')'){
                        string syms_out(1,s[i]);
                        out.syms.push_back(syms_out);
                        }
                else if (s[i] == '=' && s[i+1] == '>'){
                        string syms_out = s.substr(i, 2);
                        out.syms.push_back(syms_out);
                        i++;
                        }
                else if (i != input_size && s[i] == '<' && s[i+1] == '=' && s[i+2] == '>'){
                        string syms_out  = s.substr(i, 3);
                        out.syms.push_back(syms_out);
                        i++;
                        i++;
                        }
                else if(s[i] == ' '){
                        continue;
                        }
                else{
                        out.success = false;
                        }
		}
                out.success = true;
		
                return out;
        }

pNODE cons(string s,pNODE c1,pNODE c2){
  pNODE ret = new AST;
  ret->info = s;  // same as (*ret).info = s
  ret->children[0]=c1;
  ret->children[1]=c2;
  return ret;
}


void prinTree(AST T){
  // If both children are NULL, just print the symbol
  if (T.children[0]==NULL){
    cout<< T.info;
    return;
  }

  // print an opening paren, followed by the symbol of T, followed
  // by a space, and then the first child.
  cout << "(" << T.info<<" ";
  prinTree(*(T.children[0]));
  cout << " ";

  // print the second child if there is one, and then a right paren.
  if (T.children[1] != NULL)
      prinTree(*(T.children[1]));
  cout << ")";
}



string ASTtoString(AST T) //converts an AST to String
{
        string s;
// If both children are NULL, just print the symbol
if (T.children[0]==NULL){
s= s+ T.info;
return s;
}

// print an opening paren, followed by the symbol of T, followed
// by a space, and then the first child.
s = s+ "(";
s = s+ T.info;
s = s+ " ";
s+= ASTtoString(*(T.children[0]));
s = s+ " ";

// print the second child if there is one, and then a right paren.
if (T.children[1] != NULL){
s+= ASTtoString(*(T.children[1]));
}
s = s+ ")";
return s;
}


parseRslt parse(vector<string> V){
		
	parseRslt out;
	bool success;
	int root_node = -1;
	int this_node = 0;
	int node_mod = 0;
	int negate = 0;
	int negatedouble = 0; 
	int opperators= 0;
	int objects =0;
	int nor_objects=0;
	int this_opperators = 0;
	int root_mod;
	int node_lvl;

	std::string str1 ("(");
	std::string str2 (")");
	std::string str3 ("~");
	std::string str4 ("^");
	std::string str5 ("v");
	std::string str6 ("=>");
	std::string str7 ("<=>");
	std::string str8 ("T");
	std::string str8N ("~T");
	std::string str9 ("F");
	std::string str9N ("~F");
	vector<string>::iterator i;
	vector<string>::iterator ii;


	vector<string>::iterator dm1;
	vector<string>::iterator dm2;
	vector<string>::iterator dm3;
	
	vector<int>::iterator imp1;
	vector<int>::iterator imp2;

	vector<string>::iterator I;

	int root_loc = 0;
	int jj= 0;
	out.success == false;
	int lvl = 0;
	string superinfo;

	vector<string> Q;
	vector<int>the_tree;
	vector<int> O;
	vector<int>leafs;
	vector<int> nodes;
	vector<int> dm_lvl;
	int dm_mod;
	std::vector<int>negvec;
        negvec.push_back(node_mod);
	bool fun_n = false;
	bool demorgan = false;
	bool demorgan2 = false;
	bool demorgan3 = false;

	std::vector<int>dm_vec;
	std::vector<int>imp_vec;


	AST ast;
	int dm_count = 0;
	int dm_from = 0;
	int dm_through = 0;
	int leaf_int = 0;

	int dm_to = 0;	
	int dm_hold = 0;
	std::vector <string> v_clone;
	imp1 = leafs.begin();
	imp_vec.push_back(0);
	int failure = 0;
	int failure_at;
	failure_at = V.size();
	success = true;
	for (i = V.begin(); i != V.end(); i++){

		std::string str10 (*i);
		failure++;
		if(str7.compare(str10)== 0 || str6.compare(str10)== 0 || str5.compare(str10)== 0 || str4.compare(str10)== 0){
			opperators++;
			if (failure == failure_at || failure == 1){
				cout<< "An invalid String was entered"<<"\n";
				success = false;
				break;
				}
			if (str7.compare(str10)== 0){

				if(fun_n == true){
                			this_node = node_mod + 7;

					demorgan = true;
					dm_vec.push_back(dm_hold);
					dm_vec.push_back(lvl);
					dm_lvl.push_back(node_mod);
					dm_mod = node_mod;
					}
				else if (fun_n == false){

                			this_node = node_mod + 5;
					}
                		if(root_node <= this_node || root_node == -1){
                        		root_node = this_node;
                        		superinfo = str7;
					root_loc = lvl;
					root_mod = node_mod;
                        		}
                		

				}				
        		else if (str6.compare(str10)== 0){
				int imp_int = imp_vec.back();
				imp1 = leafs.begin() + imp_int;
				imp2 = leafs.begin() + leaf_int;
				vector<int>::iterator imp3;
				int int_sub = 0;
				int imp_lvl = 0;
				for (std::vector<int>::const_iterator Z = imp1; Z != imp2; ++Z){
					
					int_sub = *Z;	
                			vector<int>::iterator imp_x = leafs.begin() + imp_int+ imp_lvl;
					imp_lvl++;
					if(int_sub == 1){

					imp_x = leafs.erase(imp_x);
					imp_x = leafs.insert(imp_x, 3);
						}
					else if(int_sub == 2){

					imp_x = leafs.erase(imp_x);
					imp_x = leafs.insert(imp_x, 4);
						}
                        		
					else if(int_sub == 3){

					imp_x = leafs.erase(imp_x);
					imp_x = leafs.insert(imp_x, 1);
						}
					else if(int_sub == 4){

					imp_x = leafs.erase(imp_x);
					imp_x = leafs.insert(imp_x, 2);
						}

					}

				if(fun_n == false){
                			this_node = node_mod + 7;
					}
				else if(fun_n == true){
					this_node = node_mod + 8;
					}
				
                		if(root_node <=  this_node || root_node == -1){
                       			root_node = this_node;
                        		superinfo = str6;
					root_loc = lvl;
					root_mod = node_mod;
                        		}
                		
				}
        		else if (str5.compare(str10)== 0){
				if(fun_n == false){
                			this_node = node_mod + 7;
					}
				else if(fun_n == true){
					this_node = node_mod +8;
					}
                		if(root_node <= this_node || root_node == -1){
                       			root_node = this_node;
                        		superinfo = str5;
					root_loc = lvl;
					root_mod = node_mod;	
                        		}
                		}
        		else if (str4.compare(str10)== 0){
               			if(fun_n == false){
					this_node = node_mod + 8;
					}
				else if(fun_n == true){
					this_node = node_mod +7;
					}
               			if(root_node <= this_node || root_node == -1){
                        		root_node = this_node;
                        		superinfo = str4;
					root_loc = lvl;
					root_mod = node_mod;	
                       			}
                		}
			leaf_int++;
			Q.push_back(superinfo);
			O.push_back(this_node);
			leafs.push_back(0);
			nodes.push_back(this_node-node_mod);
			}
	        else if (str1.compare(str10) == 0){  // (
			
			if (fun_n == true){
				dm_hold = lvl;

				}

			node_mod = node_mod + 10;
			imp_vec.push_back(leaf_int);

        	       	}
	        else if(str2.compare(str10) == 0){  
			imp_vec.pop_back();
			if (negatedouble == node_mod){
				negvec.pop_back();
				negatedouble = negvec.back();
				fun_n = !fun_n;
				
			
				}

			if (dm_mod == node_mod && demorgan == true){

					demorgan2 = true;
					dm_lvl.pop_back();
					dm_mod = dm_lvl.back();
					dm_vec.push_back(lvl);
               				this_node = node_mod + 8;
					O.push_back(this_node - 5);
					leafs.push_back(0);
					nodes.push_back(8);
					leaf_int++;
					opperators++;					
						
				}
		
			if (demorgan == true && demorgan2 == true){
			
			dm_to = dm_vec.back();
			dm_vec.pop_back();
			dm_through = dm_vec.back();
			dm_vec.pop_back();
			dm_from = dm_vec.back();
			dm_vec.pop_back();

			dm1 = V.begin() + dm_from;
			dm2 = V.begin() + dm_through;
			
			std::string str10 (*dm2);

			lvl = dm_from;
			dm2 = V.erase(dm2);
			dm2 = V.insert(dm2, "v");
			string through_string =*dm2;
						
			dm3 = V.begin() + dm_to;
			string to_string = *dm1;

			demorgan2 = false;
			int h = dm_from - dm_to;
			vector<string>::iterator j;
               		lvl = dm_to;
			for (j = dm1; j != dm3; j++){
				std::string str10 (*j);

				i--;
				lvl--;	
	
			
				}
			}

			node_mod = node_mod-10;
			if (node_mod < 0){
				success = false;
				break;
				}
			}
		else if (str3.compare(str10) == 0){

			if(i != V.end()){
				ii = i + 1;
				dm_count++;
				std::string str10_ii(*ii);
				if (str1.compare(str10_ii) == 0){
					if (fun_n == false){
                       	        		fun_n = true;
						dm_hold = lvl;
						node_mod= node_mod + 10;
						negvec.push_back(node_mod);
						negatedouble = negvec.back();
						dm_vec.push_back(lvl);
						leaf_int++;
						lvl++;
						i++;
						}
					else if (fun_n == true){
						fun_n = false;	
						node_mod= node_mod + 10;
						negvec.push_back(node_mod);
						negatedouble = negvec.back();
						leaf_int++;
						lvl++;
						i++;
						}
					
					imp_vec.push_back(leaf_int);
                                	}
				else if (str8.compare(str10_ii) == 0){
					if (fun_n == false){

						this_node = node_mod + 1;
						O.push_back(this_node);
						nodes.push_back(3);
						leafs.push_back(3);
						leaf_int++;
						lvl++;
						i++;
						}
					else if(fun_n == true){

						this_node = node_mod + 1;
						O.push_back(this_node);
						nodes.push_back(1);
						leafs.push_back(1);
						leaf_int++;
						lvl++;
						i++;
						}
					}
				else if (str9.compare(str10_ii) == 0){
					if (fun_n == false){

						this_node = node_mod + 1;
						O.push_back(this_node);
						nodes.push_back(4);
						leafs.push_back(4);
						leaf_int++;
						lvl++;
						i++;
						}
					else if (fun_n == true){
       					this_node = node_mod + 1;
						O.push_back(this_node);
						nodes.push_back(2);
						leafs.push_back(2);
						leaf_int++;
						lvl++;
						i++;
                        	  		}
					}
				else{
					success = false;
					break;
					}
				
				}
			if (failure == failure_at){
				out.success = false;
				break;
				}
			}
		else if (str8.compare(str10) == 0){
	                if (fun_n ==false){

				this_node = node_mod + 1;
				O.push_back(this_node);
				nodes.push_back(1);
				leafs.push_back(1);
				leaf_int++;
				}
                	else if(fun_n == true){

				this_node = node_mod + 1;
				O.push_back(this_node);
				nodes.push_back(3);
				leafs.push_back(3);
				leaf_int++;
                       		}
                	}
	
		else if (str9.compare(str10) == 0){
                	if(fun_n == false){

				this_node = node_mod + 1;
				O.push_back(this_node);
				nodes.push_back(2);
				leafs.push_back(2);
				leaf_int++;
                        	}	
                	else if(fun_n == true){

				this_node = node_mod + 1;
				O.push_back(this_node);
				nodes.push_back(4);
				leafs.push_back(4);
				leaf_int++;
                        	}
                	}


		lvl++;

		}
	if(success == true){
	cout<<"\n";

	vector<int>::iterator p;

	vector<int>::iterator k;
	vector<int>::iterator kk;
	vector<int>::iterator u;
	int this_int = 0;

	u = nodes.begin();
	AST* info_1;
	AST* info_2;
	AST* info_3;
	AST* info_4;
	AST* info_5;
	AST* info_6;
	AST* info_7;
	AST* info_8;

	AST* info_1a;
	AST* info_2a;

	AST* info_l;
	AST* info_r;
	
	
	AST info_00;
	info_00 = *cons("zero", NULL, NULL);

	info_1 = cons("T", NULL, NULL);
	info_2 = cons("F", NULL, NULL);
	
	info_1a = cons("T", NULL, NULL);
        info_2a = cons("F", NULL, NULL);

	info_3 = cons("~",  info_1a, NULL);
	info_4 = cons("~", info_2a, NULL);

	int three;
	int throwback = 0;	
	vector<AST> branches;
	vector<AST>::iterator branch = branches.begin();
	vector<AST>::iterator branchend = branches.begin();
	vector<AST>the_leafs;
	branches.push_back(info_00);
	for(int zoro = 0; zoro != opperators; zoro++){


			int l_lvl = 0;
			
			int z_lvl = 0;
			int y = -1;
			int z = -1;	
			int x = -1;
			int x_lvl = 0;

		
                int y_lvl = 0;
			
                ii = Q.begin();
                std::string infofinal (*ii);
				
		p = O.begin() + root_loc - 1;

				
	       	for (k = O.begin(); k != O.end(); k++){
                        this_int = * k;
			l_lvl++;
			if (  x <=  this_int || x == -1){

				x = this_int;
				x_lvl = l_lvl;
				}
			
			
			
			}
		
		u = O.begin() + x_lvl;
	
		y = * u;
                z = * u;
		y_lvl = x_lvl -1;
		z_lvl = x_lvl +1;
                                
                vector<int>::iterator tor_y = leafs.begin() + x_lvl-2;
                vector<int>::iterator tor_x = nodes.begin() + x_lvl -1;
                vector<int>::iterator tor_subx = O.begin();
                vector<int>::iterator tor_z = leafs.begin() + x_lvl;
        
                vector<int>::iterator or_y = nodes.begin() + x_lvl-2;
                vector<int>::iterator or_z = nodes.begin() + x_lvl;
                
		int p_y = *tor_y;
                int p_xx = *tor_x;
                int p_z = *tor_z;

		int o_y = *or_y;
		int o_z = *or_z;
        			
		l_lvl = x_lvl; 
		if(y == 0){
		for (std::vector<int>::const_iterator Z = u; Z != O.begin(); --Z){
				
			this_int = * Z;
                        l_lvl--;
                 	if( y <= this_int && this_int < x){
					
                                y = this_int;
                                y_lvl =l_lvl;
			
                                }

				
			}

			}	
		
		l_lvl = x_lvl;
	
		u = O.begin() + x_lvl;	
		p = O.begin() + root_loc -1 ;
		if(z == 0){
			for (std::vector<int>::const_iterator Z = u; Z!=O.end(); ++Z){
                        	
				this_int = * Z;
                        	l_lvl++;
                        	if (z < this_int  && z < x){
                                	z = this_int;
				
                        	        z_lvl =l_lvl;
						
                                	}
                        	}
			}
		
                vector<int>::iterator zip_y = O.begin() + x_lvl-2;	
                vector<int>::iterator zip_y_y = O.begin() + x_lvl-3;
                vector<int>::iterator zip_x = O.begin() + x_lvl -1;
                vector<int>::iterator zip_z = O.begin() + x_lvl;
                vector<int>::iterator zip_z_x = O.begin() + x_lvl + 1;
		
		zip_y = O.erase(zip_y);
		zip_y = O.insert(zip_y, 0);

		zip_x = O.erase(zip_x);
		zip_x = O.insert(zip_x, 0);
	
		zip_z = O.erase(zip_z);
		zip_z = O.insert(zip_z, 0);
	
                vector<int>::iterator zap_y = leafs.begin() + x_lvl-2;
                vector<int>::iterator zap_z = leafs.begin() + x_lvl;
                vector<int>::iterator zap_x = leafs.begin() + x_lvl -1;

		the_tree.push_back(p_xx);	

		if (p_y <10 && p_z < 10){
			throwback = throwback +10;
				the_tree.push_back(p_y);
				the_tree.push_back(p_z);
				zap_x = leafs.erase(zap_x);
				zap_x = leafs.insert(zap_x, throwback);
				zap_y = leafs.erase(zap_y);
				zap_y = leafs.insert(zap_y, throwback);
				zap_z = leafs.erase(zap_z);
				zap_z = leafs.insert(zap_z, throwback);
			}	
			

		else if(10 <= p_y && p_z < 10){

			the_tree.push_back(p_y);
			the_tree.push_back(p_z);
			zap_x = leafs.erase(zap_x);
			zap_x = leafs.insert(zap_x, p_y);
			zap_z = leafs.erase(zap_z);
			zap_z = leafs.insert(zap_z, p_y);
			}
		else if(10 <= p_z && p_y < 10){
			the_tree.push_back(p_y);
			the_tree.push_back(p_z);
			zap_x = leafs.erase(zap_x);
			zap_x = leafs.insert(zap_x, p_z);
			zap_y = leafs.erase(zap_y);
			zap_y = leafs.insert(zap_y, p_z);
			}
		else if(p_y > 9 && p_z > 9){
			the_tree.push_back(p_y);
			the_tree.push_back(p_z);
				
			}

		}


	branch = branches.begin() + 1;
	 
	int one;
	int two;
	int thr3e;
	int sum_branch = the_tree.size();
	sum_branch = sum_branch/3;
	int fire;
	vector<AST> bigtree;
	vector<AST> littletree;
	for (std::vector<int>::const_iterator Z = O.begin(); Z != O.end(); ++Z){
		this_int =  *Z;
		if(this_int != 0){
			success = false;
			break;
			}
		}
	if(success == true){
	cout<<"\n";
	for(std::vector<int>::const_iterator Z = the_tree.begin(); Z != the_tree.end(); ++Z){	
		one = *Z;
		Z++;
		two = *Z;
		Z++;
		thr3e = *Z;
		AST g, f, k;
		if ( one == 0 || two == 0 ||  thr3e == 0){
			success = false;
			break;
			}
		string sting;
			if (one == 8){
				sting = "^";
				}
			else if (one == 7){
				sting = "v";
				}
			else if (one == 6){
				sting = "=>";
				}
			else if (one == 5){
				sting = "<=>";
				}
			if (two == 1){
				info_l = info_1;
				}
			else if (two == 2){
				info_l = info_2;
				}
			else if (two == 3){
				info_l = info_3;
				}
			else if (two == 4){
				info_l = info_4;
				}
			if (thr3e == 1){
				info_r = info_1;
				}
			else if (thr3e == 2){
				info_r = info_2;
				}
			else if (thr3e == 3){
				info_r = info_3;
				}
			else if (thr3e == 4){
				info_r = info_4;
				}
		if (two <10 && thr3e < 10){	
			g =* cons(sting, info_l, info_r);	
			bigtree.push_back(g);
			}

		else{
	
			if(two >thr3e && thr3e < 10){
				int find = two/10;
				find--;
				vector<AST>::iterator branch = bigtree.begin() +find;
				f = *branch;
				find--;
				g.info = sting;

				g.children[0] = cons(f.info, f.children[0], f.children[1]); 
				g.children[1] = info_r;
				
				branch = bigtree.erase(branch);
				branch = bigtree.insert(branch, g);
				bigtree.push_back(g);
				}
			else if (thr3e > two && two < 10){
				int find = thr3e/10;
				find--;
				vector<AST>::iterator branch = bigtree.begin() +find;
				f = *branch;
				g.info = sting;
				g.children[1] = cons(f.info, f.children[0], f.children[1]); 
				g.children[0] = info_l;
				branch = bigtree.erase(branch);
				branch = bigtree.insert(branch, g);
				}
			else if(two < thr3e){
				int find1 = two/10;
				int find2 = thr3e/10;
				find1--;
				find2--;	
				vector<AST>::iterator branch = bigtree.begin() +find1;
				vector<AST>::iterator branchend = bigtree.begin() +find2;
				f = *branch;
				k = *branchend;

				g.info = sting;
				g.children[0] = cons(f.info, f.children[0], f.children[1]); 
				g.children[1] = cons(k.info, k.children[0], k.children[1]);
				branchend = bigtree.erase(branchend);
				branchend = bigtree.insert(branchend, g);
				branch = bigtree.erase(branch);
				branch = bigtree.insert(branch, g);
				}
			else if(two > thr3e){
				int find1 = two/10;
				int find2 = thr3e/10;
				find1--;
				find2--;	
				
			
				vector<AST>::iterator branch = bigtree.begin()+find1;

				vector<AST>::iterator branchend = bigtree.begin() +find2;

				f = *branch;
				k = *branchend;

				
				g.info = sting;
				g.children[0] = cons(f.info, f.children[0], f.children[1]); 
				g.children[1] = cons(k.info, k.children[0], k.children[1]);
				branch = bigtree.erase(branch);
				branch = bigtree.insert(branch, g);
				branchend = bigtree.erase(branchend);
				branchend = bigtree.insert(branchend, g);
				}
			int four = bigtree.size();
			ast = g;
			}
		ast = g;
	prinTree(g);
		}

		}


	else{
		cout<<"\n";

		}

		}

	else{
		cout<<"\n";

		}
	out.success = success;
	out.ast = ast;

	cout<<"____________________________-"<<"\n";
	return out;
	
	}	

TPERslt TPE(string s){
	TPERslt out;
	tokRslt results = tokenize(s);
	parseRslt results1 = parse(results.syms);
	out.val = results.success;
	if(results1.success == true && results.success == true){
		out.msg = "success";
		}
	else if(results.success == false){
		out.msg = "grammar error";
		}
	else if(results1.success == false){
		out.msg = "symbol error";
		}
	return out;
}



bool eval(AST T){
	bool info_eval;
	bool c0;
	bool c1;
	if (T.children[0]==NULL || T.children[1] == NULL){
		if (T.children[0]==NULL && T.children[1] == NULL){
			if (T.info == "T"){
				info_eval = true;
				}
	 		else if(T.info == "F"){
				info_eval = false;
				}	
			}
	
		else if(T.info == "~"){
			c0 = eval(*T.children[0]);
			if(c0 == true){
				info_eval = false;

				}
			else if(c0 == false){
				info_eval = true;
				}
			}
		} 
	else{
		c0 = eval(*T.children[0]);
		c1 = eval(*T.children[1]);
		if(T.info == "^"){
			if(c0 == c1 && c1 == true){
				info_eval = true;
				}
			else{
				info_eval = false;
				}
			}
		else if(T.info == "v"){
			if(c0 == c1 && c0 == false){
				info_eval = false;
				}
			else{
				info_eval = true;
				}
			}
		else if(T.info == "<=>"){
			if(c0 == c1){
				info_eval = true;
					}
			else{
				info_eval = false;
					}
				}
			
			}
		return info_eval;
	}		

void checkTokenize()
{
	tokRslt tk1,tk2;
	string s1="=><=>";
	string s2="(T v F)";
	vector<string> v1,v2;
	
	tk1=tokenize(s1);
	tk2=tokenize(s2);
	
	if(tk1.success && tk2.success)
	{
		v1.push_back("=>"); //if the success value is true only then we initialize vectors v1,v2 with actual input symbols
		v1.push_back("<=>");
		
		v2.push_back("(");
		v2.push_back("T");
		v2.push_back("v");
		v2.push_back("F");
		v2.push_back(")");
		
		if(tk1.syms== v1 && tk2.syms== v2)
			cout<<"\nTokenize ALL Test Cases passed";
	
		else if(tk1.syms!= v1)
		{
			cout<<"\nTokenize Test case 1: "<<s1<<" FAILED";
		}
		
		else if(tk2.syms!= v2)
		{
			cout<<"\nTokenize Test case 2: "<<s2<<" FAILED";
		}
		else
		{
			cout<<"\nTokenize ALL test cases FAILED";
		}
	}

	else if(!tk1.success)
	{
		cout<<"\nTokenize Test case 1: "<<s1<<" FAILED";
	}
	else if(!tk2.success)
	{
		cout<<"\nTokenize Test case 1: "<<s1<<" FAILED";
	}
	else
	{
			cout<<"\nTokenize ALL test cases FAILED";
	}
}

void checkParse()
{
	vector<string> v1,v2;
	parseRslt pr1,pr2;
	
	string s1="T v F ^ F";
	string s2="~F ^ T";
	
	v1.push_back("T"); //v1 = T v F ^ F
	v1.push_back("v");
	v1.push_back("F");
	v1.push_back("^");
	v1.push_back("F");
	
	v2.push_back("~"); //v2 = ~F ^ T
	v2.push_back("F"); //v2 = ~F ^ T
	v2.push_back("^");
	v2.push_back("T");
	
	pr1=parse(v1);
	pr2=parse(v2);
	
	if(pr1.success && pr2.success)
	{
		string AST_case1 = "(v T (^ F F))";  //AST for v1 = T v F ^ F
		string AST_case2 = "(^ (~ F ) T)"; //AST for v2 = ~F ^ T
		string pr1_str,pr2_str;

		//Converting user AST tree to string for comparison 
		pr1_str=ASTtoString(pr1.ast); 
		pr2_str=ASTtoString(pr2.ast);
		
		if(pr1_str == AST_case1 && pr2_str == AST_case2)
		{
			cout<<"\nParse ALL Test cases Passed";
		}
		
		else if(pr1_str != AST_case1)
		{
			cout<<"\nParse Test case 1: "<<s1<<" FAILED";
		}
		else if(pr2_str != AST_case2)
		{
			cout<<"\nParse Test case 2: "<<s2<<" FAILED";
		}
		
		else
		{
			cout<<"\nParse ALL Test case FAILED";
		}
	}
	
	else if(!pr1.success)
	{
		cout<<"\nParse Test case 1: "<<s1<<" FAILED";
	}
	else if(!pr2.success)
	{
		cout<<"\nParse Test case 2: "<<s2<<" FAILED";
	}
	else
	{
			cout<<"\n Parse ALL test cases FAILED";
	}
	
}

void checkEval()
{
	bool ev1,ev2;
	AST test1,test2,B,C,D,E,b,c,d,e;
	string s1="T v F ^ F";
	string s2="~ F ^ T";
	//AST for T v F ^ F
	test1= *cons("v",&B,&C); 
	B= *cons("^",&D,&E);	
	C= *cons("T",NULL,NULL);
	D= *cons("F",NULL,NULL);
	E= *cons("F",NULL,NULL);
	

	//AST for ~ F ^ T
	test2= *cons("^",&b,&c); 
	b= *cons("~",&d,NULL);	
	c= *cons("T",NULL,NULL);
	d= *cons("F",NULL,NULL);
	
	
	ev1=eval(test1);
	ev2=eval(test2);
	
	if(ev1 && ev2)
	{
		cout<<"\nEval ALL Test cases Passed";
	}
	else if(!ev1)
	{
		cout<<"\nEval Test case 1: "<<s1<<" FAILED";
	}
	else if(!ev2)
	{
		cout<<"\nEval Test case 2: "<<s2<<" FAILED";
	}
	else
	{
		cout<<"\nEval ALL test cases FAILED";
	}
	
}


string TPEOut(string s){
	tokRslt results = tokenize(s);
	parseRslt results1 = parse(results.syms);
	bool ev;
	string out;
	if(results1.success == true && results.success == true){
		ev = eval(results1.ast);
		if (ev == true){
			out = "true";
			}
		else if(ev == false){
			out= "false";
			}
		}
	if(results1.success == false){
		out = "grammar error";
		}
	else if(results.success == false){
		out = "symbol error ";
		}
	return out;
}

void checkTPE()
{
	TPERslt tpe1,tpe2;
	tpe1=TPE("TvT^F->F"); //Should evaluate to TRUE
	tpe2=TPE("T v F * F"); //Should print "symbol error"
	
	if(tpe1.msg == "success" && tpe2.msg=="symbol error")
	{
		if(tpe1.val) //if AST evaluates to TRUE for test case 1-     T => ~F
			cout<<"\nTPE ALL Test cases PASSED";
	}
	else if(!tpe1.val)
	{
		cout<<"\nTPE Test case 1: T => ~F "<<" FAILED";
	}
	else if(tpe2.msg!="symbol error")
	{
		cout<<"\nTPE Test case 2: T v F * F "<<" FAILED";
	}
	else
	{
		cout<<"\nTPE ALL test cases FAILED";
	}
}

void checkTPEOut()
{
	string t1,t2;
	
	string case1= "TvT^F->F"; //Should evaluate to "false"
	string case2= "(T v F) v ~ F ^ F"; //Should evaluate to "true"
	
	t1=TPEOut(case1);
	t2=TPEOut(case2);
	
	if(t1 == "false" && t2=="true")
	{
		cout<<"\nTPEOut ALL Test cases PASSED";
	}
	else if(t1!="false") 
	{
		cout<<"\nTPEOut Test case 1: "<<case1<<" FAILED";
	}
	else if(t2!="true") 
	{
		cout<<"\nTPEOut Test case 2: "<<case2<<" FAILED";
	}
	else
	{
		cout<<"\nTPE ALL test cases FAILED";
	}
}


	
int main()
{
//	checkTokenize();
//	checkParse();
	//checkEval();
//	checkTPE();
	checkTPEOut();

//Running cusotm check
	string user_input;
        string test_TPEOut;
	
//	bool ev1=eval("(T v F) v ~ F ^ F");
       	cout<<"SHOW? "<< eval <<" \n";	
			
       	cout << "Please enter a string:";
        getline(cin, user_input);
        TPERslt test_TPE = TPE(user_input);
        cout<<"MAJOR check 1"<<"\n";
        test_TPEOut = TPEOut(user_input);
	
        cout<<"MAJOR check 2"<<"\n";
        cout<<test_TPEOut <<"\n";

	return 0;
}


//((T^F)<=>Tv~F)v(T^(TvF))
//((((TvT)vF)v~T)^(((FvF)^T)^T)=>(((T<=>T)v~F)=>~T))
//~((TvT)vT)<=>T




