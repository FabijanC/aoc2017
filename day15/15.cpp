#include <iostream>
#include <vector>
#define MOD 2147483647
#define PA 16807
#define PB 48271
#define SEEDA 783
#define SEEDB 325
#define LIMIT 5000000
using namespace std;
typedef long long ll;

int main() {
    ll a = SEEDA, b = SEEDB;
    vector<ll> va, vb;
    int printcnt = 0;
    while ((va.size() < LIMIT) || (vb.size() < LIMIT)) {
        a = (a * PA) % MOD;
        b = (b * PB) % MOD;

        if (!(a & 0b11)) {
            va.push_back(a);
            //cout << "va ->" << va.size() << endl;
        }
        if (!(b & 0b111)) {
            vb.push_back(b);
            //cout << "vb ->" << vb.size() << endl;
        }
        
        //if ((va.size() % 10000 == 0) && (printcnt % 5000 == 0)) {cout << va.size() << " " << vb.size() << endl; ++printcnt;}
    }
    cout << va.size() << " " << vb.size() << endl;
    int cnt = 0;
    for(int i = 0; i < LIMIT; ++i) {
        if ((va[i] & 0xffff) == (vb[i] & 0xffff)) {
            ++cnt;
        }
    }
    
    cout << cnt << endl;
    
    return 0;
}