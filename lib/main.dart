import 'package:flutter/material.dart';
import 'pages/searchPage.dart';





void main(){
  runApp(VSM());
}




class VSM extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return MaterialApp(
    debugShowCheckedModeBanner: false,
    title:'VSM Model',
    //theme: ThemeData(
    //  fontFamily: 
    //),
    home: SearchPage(),
    
    );
  }
}





