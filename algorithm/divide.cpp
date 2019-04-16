//
// Created by ASUS on 2019/4/16.
//

#include <iostream>
#include <vector>
using namespace std;

int binarySearch(vector<int> &v,int key){
    //    vector<int> v={1,2,3,4,5,6,7};
    //    cout<<binarySearch(v,13);
    //    return 0;
    int low=0,high=v.size()-1;
    int mid ;
    while(low<=high){
        mid = (low+high)/2;
        if(v[mid]==key)
            return mid;
        else if(v[mid]>key)
            high = mid - 1;
        else
            low = mid + 1;
    }
    return -1;
}

void merge(vector<int> &v,int low,int high, vector<int>&temp){
    int mid=(low+high)/2;
    int i=low;
    int j=mid+1;
    int t=0;
    while (i<=mid && j<=high){
        if(v[i]>v[j])
            temp[t++]=v[i++];
        else
            temp[t++]=v[j++];
    }
    while (i<=mid)
        temp[t++]=v[i++];
    while(j<=high)
        temp[t++]=v[j++];
    t=0;
    while(low<=high)
        v[low++]=temp[t++];
}
void mergeSort(vector<int> &v,int low,int high, vector<int>&temp){
    //    vector<int> v={1,12,3,24,5,36,7};
    //    vector<int> temp(v.size(),0);
    //    mergeSort(v,0,v.size(),temp);
    //    for(int i:v)
    //        cout<<i<<' ';
    if(low<high){
        int mid=(low+high)/2;
        mergeSort(v,low,mid,temp);
        mergeSort(v,mid+1,high,temp);
        merge(v,low,high,temp);
    }
}


int main(){
    vector<int> v={1,12,3,24,5,36,7};
    vector<int> temp(v.size(),0);
    mergeSort(v,0,v.size(),temp);
    for(int i:v)
        cout<<i<<' ';
    return 0;
}