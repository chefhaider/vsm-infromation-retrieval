import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:http/http.dart' as http;

//import 'package:app/api.dart';
import 'dart:convert';


class SearchPage extends StatefulWidget {
  @override
  _SearchPageState createState() => _SearchPageState();
}

class _SearchPageState extends State<SearchPage> {
  String url;
  List data;
  String queryText = 'Query';



  List doc = [];
  List score = [];


  @override
  Widget build(BuildContext context) {
    return Scaffold(

      
      appBar: AppBar(
        centerTitle: true,
        toolbarHeight: 70,
        title: Text('Vector Space Model',style: GoogleFonts.getFont('Megrim',fontSize: 0.04*MediaQuery.of(context).size.width,color: Colors.black)),

        flexibleSpace: Container(
          decoration: BoxDecoration(
            gradient: LinearGradient(
              begin: Alignment.topLeft,
                end: Alignment.bottomRight,
                colors: <Color>[
                  Colors.red,
                  Colors.blue
                ])          
              ),     

          ),   
      ),

      body: Center(
      
        child:Column(

          
          children : [

            SizedBox(
                height: 80,
              ),

            Container(

              

              width:0.5*MediaQuery.of(context).size.width,
              child:TextField(
                
                onSubmitted :  (value) async {
                  
                  
                  
                  if (value != '')  {

                    url = 'http://127.0.0.1:5000/search?Query=' + value.toString();
                    final response = await http.get(Uri.parse(url));
                    final decoded = json.decode(response.body) as Map<String, dynamic>;
                    
                    setState(()  {
                      
                        doc = (decoded['doc']);
                        score = (decoded['score']);

                      });

                  }
                },
                

                decoration: InputDecoration(
                  
                  hintText: 'Type a Query and hit Enter',
                  suffixIcon: Icon(Icons.search),
                  enabledBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(30),
                        borderSide: BorderSide(
                          color: Colors.red,
                          width: 1.0,
                        ),
                      ),
                      focusedBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(10),
                        borderSide: BorderSide(
                          color: Colors.blue,
                          width: 2.0,
                        ),
                      ),
            

                  ),
              )),

              SizedBox(
                height: 10,
              ),


              Expanded(
                
                child: ListView.separated(
                padding: const EdgeInsets.fromLTRB(50,30,50,0),
                itemCount: doc.length,
                itemBuilder: (context, index) {
                  
                  return Container(
                    height: 30,
                    color: Colors.indigo[50],
                    child: Center(child: Text('doc id ${doc[index]} with '+'similarity score ${score[index]}')),
                  );
                },
                separatorBuilder: (BuildContext context, int index) => const Divider(),
              ),
              ),
            ],
        ),

      ),
    );
  }
}