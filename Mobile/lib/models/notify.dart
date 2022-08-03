import 'package:flutter/material.dart';
import 'package:rsdb/models/colors.dart';

void alert(String message, BuildContext context,{Color color = bgColor} ){
  ScaffoldMessenger.of(context).showSnackBar(
    SnackBar(
      elevation: 0.0,
      behavior: SnackBarBehavior.floating,
      content: Align(
        alignment: Alignment.center,
        child: Container(
          width: 200,
          height: 40.0,
          decoration: BoxDecoration(
            color: color,
            borderRadius: BorderRadius.circular(20.0),
            border: Border.all(width: 0.5, color: Colors.black),
          ),
          child: Center(child: Text(message)),
        ),
      ),
      duration: const Duration(seconds: 3),
      backgroundColor: Colors.transparent,
    ),
  );
}
