#include "TFile.h"
#include "TH1.h"
#include "TH2.h"
#include "TTree.h"
#include <TRandom.h>
#include <TCanvas.h>
#include <TStyle.h>
#include <Riostream.h>




void render2(char *name="NOTHING", char *rootFile="render2.root")
{


 printf("The argument is %s\n", name);
 printf("The second argument is %s\n", rootFile);

TFile *f = new TFile(rootFile,"UPDATE");

TTree *render2 = new TTree("render2","Tree data");

render2->Write("render2",TObject::kOverwrite);


	Int_t d1, d2,count,ot;

	Int_t dect1,dect2;

	Double_t Adect1,Adect2;

	Int_t BIASmax, BIASmin;

	BIASmax=5005;

	BIASmin=0;


render2->Branch("ADetector1render2",&Adect1,"Adect1/D");
render2->Branch("ADetector2render2",&Adect2,"Adect2/D");
render2->Branch("OT",&ot,"OT");




FILE *out;

out=fopen(name,"r");
printf("opening %s\n",name);

while(!feof(out))  {

	fscanf(out,"%d\t%d\t%d",&d1,&d2,&ot);
	count++;
	Adect1 = d1;
	Adect2 = d2;
/*
	if (d1<BIASmax && d1>BIASmin) {

		dect1=d1;
		Adect1=(1.0*dect1)+0;

	}

	        dect2=0;
		Adect2=0;

		dect2=d2;
		Adect2=(1.0*dect2)+0;

	}

*/

render2->Fill();

}

cout << "The Number of Events is: " << count <<endl;

fclose(out);


f->Write("",TObject::kOverwrite);


}
