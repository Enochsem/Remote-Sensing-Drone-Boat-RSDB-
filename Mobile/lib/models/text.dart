import 'package:flutter/material.dart';
import 'package:rsdb/models/colors.dart';


Widget titleText(String text, {double size = 18}){
  return Center(
    child: Text(
      text,
      style: TextStyle(
        color: pink,
        fontSize: size,
        fontWeight: FontWeight.bold,
      ),
    ),
  );
}


Widget text(String text,Color color, {double size = 18}){
  return Padding(
    padding: const EdgeInsets.all(10.0),
    child: Text(
      text,
      style: TextStyle(
        color: color,
        fontSize: size,
        fontWeight: FontWeight.bold,
      ),
    ),
  );
}
