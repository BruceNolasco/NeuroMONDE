#include <stdio.h>
#include <math.h>
#include <string.h>
#include <errno.h>
#define PI 3.14159265
#define E 2.718281828
// 0 = lower    1 = llc     2 = left
// 3 = ulc      4 = upper   5 = urc
// 6 = right    7 = lrc
//vector with vector x,y position and an int code for orientation
float dList [][3]= {
  {79.35,0,0},
  {49.35,0,0},
  {34.35,0,0},
  {2.5,2.5,1},
  {0,35,2},
  {2.5,67.5,3},
  {34.35,70,4},
  {49.35,70,4},
  {79.35,70,4},
  {109.35,70,4},
  {124.35,70,4},
  {156.35,67.5,5},
  {158.7,35,6},
  {156.2,2.5,7},
  {124.35,0,0},
  {109.35,0,0}
  };

float absF (float n){
  if(n >=  0)
    return n;
  else
    return -n;
}

//given a point gets distance to that detector
float getR( float xS, float yS, int detector)
{
  float r = sqrt( ( pow(dList[detector][0]-xS,2) + pow(dList[detector][1]-yS,2) ) );
  return r;
};

//given a point gets the angle from that detector
float getTheta (float xS ,float yS, int detector)
{
  float theta,vx,vy,cosTheta;
  int id = dList[detector][2];
  xS -= dList[detector][0];
  yS -= dList[detector][1];
  //lower
  if(id == 0)
  {
    vx = 1;
    vy = 0;
  }
  else
  {
    if(id == 1)
    {
      vx = 1/(sqrt(2));
      vy = -1/(sqrt(2));
    }
    else
    {//left
      if(id == 2)
      {
        vx = 0;
        vy = -1;
      }
      else
      {
        //upper left corner
        if(id == 3)
        {
          vx = -1/(sqrt(2));
          vy = -1/(sqrt(2));
        }
        else
        {
          //upper
          if(id == 4)
          {
            vx = -1;
            vy = 0;
          }
          else
          { //upper right corner
            if(id == 5)
            {
              vx = -1/(sqrt(2));
              vy = 1/(sqrt(2));
            }
            else
            {//right
              if(id == 6)
              {
                vx = 1;
                vy = 0;
              }
              else
              {//lower tight corner
                if(id == 7)
                {
                  vx = 1/(sqrt(2));
                  vy = 1/(sqrt(2));
                }
                else
                {
                  printf("Incorrect detector position ID\n");
                }
              }
            }
          }
        }
      }
    }
  }
  cosTheta = (xS*vx+yS*vy)/sqrt(pow(xS,2)+pow(yS,2));
  theta = acos(cosTheta);

  return theta;
}

float getSignalForD (float xs, float ys, int detector)
{
  float A, gamma, lam, thetaC, r , theta, S;
  float sub1,sub2;
  //Parameter for signal computing
  //Amplification parameter
  A = 100000;
  //Dimensionality
  gamma = 1.3;
  lam = 21;
  //Angular amplitude of detector
  thetaC = PI/6;
  //get the distance and angle to that detector
  r = getR(xs,ys,detector);
  theta = getTheta(xs,ys,detector);
  //Check if signals in sight field of detector
  if((theta > 0 && theta < thetaC)||(theta < PI && theta > PI - thetaC))
  {
    //printf("Theta out of value");
    S = 0;
  }
  else
  {
    sub1 = sin(PI*(theta-thetaC)/(PI-2*thetaC));
    //printf("Sub1 (sins): %f\n",sub1);
    sub2 = pow(r,gamma);
    //printf("Sub3 (%.2f^%.2f): %f\n",r,gamma,sub2);
    //Equation for signals computing
    S = A*(exp(-r/lam))*(abs(sub1))/sub2;
  }
  return S;
}

int main ()
{
  //Files for point list and relative signaals
  FILE *relSignalsFile;
  FILE *pointListFile;
  //char relSName[51];
  char opt;
  errno = 0;
  //counters
  int d,max;
  float i,j;
  //signals vector and delimiting coordinates
  float sig[16],maxS,top,bot,left,right,res;

  printf("Welcome to MONDE@C Relative Signal Generator\n");
  //printf("Please enter the name of the file(s)\n");
  //scanf("%s",&relSName);
  fflush(stdin);

  printf("\nPlease enter the inital coordinates x,y\n");
  scanf("%f,%f",&left,&bot);
  fflush(stdin);

  printf("\nPlease enter the final coordinates x,y\n");
  scanf("%f,%f",&right,&top);
  fflush(stdin);

  printf("\nPlease enter the resolution in cm.\n");
  scanf("%f",&res);

  printf("\nComputing ");

  relSignalsFile = fopen("relSignalsC.txt","w+");

  if(relSignalsFile == NULL)
    printf("relSignalsFile NULL pointer (%d)\n",errno);
  errno = 0;

  //strcat(relSName,"PL");
  pointListFile = fopen("pointListC.txt","w+");

  if(pointListFile == NULL)
    printf("pointListFile NULL pointer (%d)\n",errno);

  printf("Files: %p ; %p\n",relSignalsFile,pointListFile);
  printf("from %f,%f to %f,%f\n",left,bot,right,top);

  for (i = left; i <=right; i+=res)
  {
    for (j = bot; j <= top; j+=res)
    {
      max = 0;
      maxS =0;
      for (d = 0; d<16; d++)
      {
        sig[d] = getSignalForD(i,j,d);
        if (sig[d]>=maxS)
        {
          maxS = sig[d];
          max = d;
        }
      }
      printf("\n Signals for %f,%f\n",i,j);
      printf("\n");
      fprintf(pointListFile, "%.2f %.2f\n",i,j);
      for (d = 0; d<16; d++)
      {
        printf(" %f\t",sig[d]);
        sig[d]=sig[d]/maxS;
        printf("%f\n",sig[d]);
        fprintf(relSignalsFile,"%f",sig[d]);
        if(d!=15)
          fprintf(relSignalsFile,"\t");
      }
      fprintf(relSignalsFile, "\n");

    }
  }
  fclose(relSignalsFile);
  fclose(pointListFile);
  return 0;
}
