// Exhaustive evaluator for Graffiti 195 and 219 on graph6 input (connected graphs, n<=20).
// usage: geng ... | ./exh 195   or ./exh 219
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MAXN 24
static int n; static int A[MAXN][MAXN]; static int D[MAXN][MAXN]; static int deg[MAXN];
static int parse(char*s){ n=s[0]-63; if(n<1||n>=MAXN) return 0; memset(A,0,sizeof A);
 int k=0; char*p=s+1; int bits=0,cur=0;
 for(int j=1;j<n;j++) for(int i=0;i<j;i++){ if(bits==0){cur=*p++-63;bits=6;} bits--; if((cur>>bits)&1){A[i][j]=A[j][i]=1;} k++; }
 for(int i=0;i<n;i++){deg[i]=0;for(int j=0;j<n;j++)deg[i]+=A[i][j];} return 1;}
static void bfs(){ for(int s=0;s<n;s++){ int q[MAXN],h=0,t=0; for(int i=0;i<n;i++)D[s][i]=-1; D[s][s]=0;q[t++]=s;
  while(h<t){int u=q[h++]; for(int v=0;v<n;v++) if(A[u][v]&&D[s][v]<0){D[s][v]=D[s][u]+1;q[t++]=v;}}}}
// Jacobi eigenvalues of symmetric matrix M (n x n), returns in ev
static void jacobi(double M[MAXN][MAXN], int N, double*ev){
 double a[MAXN][MAXN]; memcpy(a,M,sizeof(a));
 for(int sweep=0;sweep<100;sweep++){ double off=0; for(int i=0;i<N;i++)for(int j=i+1;j<N;j++)off+=a[i][j]*a[i][j];
  if(off<1e-22) break;
  for(int p=0;p<N;p++)for(int q=p+1;q<N;q++){ if(fabs(a[p][q])<1e-300) continue;
   double th=(a[q][q]-a[p][p])/(2*a[p][q]); double t=(th>=0?1:-1)/(fabs(th)+sqrt(th*th+1)); double c=1/sqrt(t*t+1), s=t*c;
   for(int k=0;k<N;k++){ double akp=a[k][p], akq=a[k][q]; a[k][p]=c*akp-s*akq; a[k][q]=s*akp+c*akq; }
   for(int k=0;k<N;k++){ double apk=a[p][k], aqk=a[q][k]; a[p][k]=c*apk-s*aqk; a[q][k]=s*apk+c*aqk; }
  }}
 for(int i=0;i<N;i++) ev[i]=a[i][i];
}
static double lam1_adj(){ // power iteration on A+I, high precision
 double x[MAXN],y[MAXN]; for(int i=0;i<n;i++) x[i]=1.0+0.01*i; double lam=0,prev=-1;
 for(int it=0;it<20000;it++){ double nr=0; for(int i=0;i<n;i++){ double s=x[i]; for(int j=0;j<n;j++) if(A[i][j]) s+=x[j]; y[i]=s; nr+=s*s;}
  nr=sqrt(nr); double num=0,den=0; for(int i=0;i<n;i++){num+=x[i]*y[i];den+=x[i]*x[i];} lam=num/den-1; for(int i=0;i<n;i++) x[i]=y[i]/nr;
  if(fabs(lam-prev)<1e-13 && it>50) break; prev=lam; }
 return lam; }
int main(int argc,char**argv){ int conj=atoi(argv[1]); char line[1024]; long cnt=0,cond=0,cand=0;
 double best=-1e9; char bestg[1024]=""; double bestw=-1e9; char bestwg[1024]=""; long condw=0; double bestr=-1e9; char bestrg[1024]="";
 while(fgets(line,sizeof line,stdin)){ line[strcspn(line,"\n")]=0; if(!parse(line)) continue; cnt++; bfs();
  int m=0; for(int i=0;i<n;i++) m+=deg[i]; m/=2;
  if(conj==195){ long ev=0,od=0; int maxev=0;
   for(int v=0;v<n;v++){int e=0; for(int u=0;u<n;u++) if(u!=v){ if(D[v][u]%2==0) e++; else od++; } ev+=e; if(e>maxev)maxev=e;}
   // relaxed: ignore condition
   int ok = (od<=ev); if(ok) cond++;
   int okw = (od<=ev+n); if(okw) condw++;  // WoW def: even vector includes the vertex itself
   // cheap upper bound: lam1 <= max_v sqrt(sum_{u~v} d_u)
   double ub=0; for(int v=0;v<n;v++){ double s=0; for(int u=0;u<n;u++) if(A[v][u]) s+=deg[u]; if(sqrt(s)>ub) ub=sqrt(s);}
   int need = (ok && ub > maxev + best - 1e-12) || (okw && ub > maxev + 1 + bestw - 1e-12);
   if(need){ double l=lam1_adj(); cand++; double mg=l-maxev; if(ok && mg>best){best=mg; strcpy(bestg,line);} if(okw && mg-1>bestw){bestw=mg-1; strcpy(bestwg,line);} }
  } else { // 219
   double G[MAXN][MAXN]; double F=0; for(int i=0;i<n;i++)for(int j=0;j<n;j++){ G[i][j]= (i==j||D[i][j]<0)?0: (double)deg[i]*deg[j]/((n-1.0)*D[i][j]); F+=G[i][j]*G[i][j]; }
   double other=n*(n-1)/2.0-m; double ub=sqrt(F/2.0);
   if(ub-other > best){ double ev[MAXN]; jacobi(G,n,ev); double l1=-1e18,l2=-1e18; for(int i=0;i<n;i++){ if(ev[i]>l1){l2=l1;l1=ev[i];} else if(ev[i]>l2) l2=ev[i]; }
     cand++; double mg=l2-other; if(mg>best){best=mg;strcpy(bestg,line);} }
  }
 }
 printf("conj %d graphs %ld cond %ld eig-evals %ld best_margin %.10f graph %s\n",conj,cnt,cond,cand,best,bestg);
 if(conj==195) printf("WoW-def(195): condw %ld best_margin_wow %.10f graph %s\n",condw,bestw,bestwg);
 return 0; }
