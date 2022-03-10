import processing.net.*;

import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;


Client myClient; 
String dataIn = "1,1,1,1,1,1"; 
int data;

public void setup(){
  size( 1280,720);
  myClient = new Client(this, "127.0.0.1", 5000);
  noLoop();
}

//Should be named s
public Float[] stringToTuple(String str){
   String[] tp = str.split(",");
   Float n1 = Float.parseFloat(tp[0]);
   Float n2 = Float.parseFloat(tp[1]);
   Float n3 = Float.parseFloat(tp[2]);
   Float n4 = Float.parseFloat(tp[3]); 
   Float n5 = Float.parseFloat(tp[4]); 
   Float n6 = Float.parseFloat(tp[5]);
   Float[] array = new Float[] {n6,n5,n4, n3, n2, n1};
   return(array);
}

public void draw(){
  background(250);
  myClient = new Client(this, "127.0.0.1", 5000);


  Float[] coords = stringToTuple(dataIn);
  fill(0);
  Float widths = abs(coords[4]-coords[2]);
  Float heigth = abs(coords[5]-coords[3]);
  rect(coords[2], coords[3], widths , heigth);
  
  

 
}

void clientEvent(Client someClient) {

  dataIn = someClient.readString();
  print(dataIn);
  redraw();
}
