import 'package:rsdb/models/login.dart';
import 'package:rsdb/models/inputs.dart';
import 'package:rsdb/models/buttons.dart';
import 'package:rsdb/models/notify.dart';
import 'package:rsdb/models/text.dart';
import 'package:flutter/material.dart';

class Signup extends StatefulWidget {
  const Signup({Key? key}) : super(key: key);

  @override
  State<Signup> createState() => _SignupState();
}

class _SignupState extends State<Signup> {
  final _formKey = GlobalKey<FormState>();

  User user = User();
  String message = "";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        padding: const EdgeInsets.all(5.0),
        child: ListView(
          children: [
            const SizedBox(
              height: 5.0,
            ),
            titleText("Sign up",size: 30.0),
            Image.asset(
              "images/signup.png",
              height: 230.0,
            ),
            Form(
              key: _formKey,
              child: Column(
                children: [
                  const SizedBox(
                    height: 5.0,
                  ),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceAround,
                    children: [
                      HalfInput(
                        obscureText: true,
                        label: "User ID",
                        hint: "Enter User ID",
                        keyboardType: TextInputType.name,
                        validator: (value) {
                          if (value == null || value.isEmpty){
                            return 'User ID is required';
                          }else if(value.length < 6){return 'At least 6 characters long';}
                          _formKey.currentState?.save();
                          return null;
                        },
                        onSaved: (String? value) {
                          user.user_id = value;
                        },
                      ),
                      HalfInput(
                        obscureText: true,
                        label: "Device ID",
                        hint: "Enter Device ID",
                        keyboardType: TextInputType.text,
                        validator: (value) {
                          if (value == null || value.isEmpty) {
                            return 'Device ID is required';
                          }
                          _formKey.currentState?.save();
                          return null;
                        },
                        onSaved: (String? value) {
                          user.device_id = value;
                        },
                      ),
                    ],
                  ),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceAround,
                    children: [
                      HalfInput(
                        obscureText: true,
                        label: "Password",
                        hint: "Enter PassWord",
                        keyboardType: TextInputType.visiblePassword,
                        validator: (value) {
                          if (value == null || value.isEmpty){
                            return 'password is required';
                          }else if(value.length < 6){return 'At least 6 characters long';}
                          _formKey.currentState?.save();
                          return null;
                        },
                        onSaved: (String? value) {
                          user.password = value;
                        },
                      ),
                      HalfInput(
                        obscureText: true,
                        label: "Confirm Password",
                        hint: "Enter Password again",
                        keyboardType: TextInputType.visiblePassword,
                        validator: (value) {
                          if (value == null ||
                              value.isEmpty ||
                              user.password != user.confirmPassword) {
                            return 'Password Mismatch';
                          }
                          _formKey.currentState?.save();
                          return null;
                        },
                        onSaved: (String? value) {
                          user.confirmPassword = value;
                        },
                      ),
                    ],
                  ),
                  const SizedBox(height: 10.0,),
                  AcknowledgeButton(
                    name: "Signup",
                    onPressed: () async {
                      if (_formKey.currentState!.validate()) {
                        _formKey.currentState?.save();
                        // print("bool check type ${user.acceptTerms.runtimeType}");
                        // print("user ==> ${user.title}\n${user.firstName}\n ${user.lastName}\n ${user.email} ${user.phoneNumber} ${user.password} ${user.acceptTerms}");

                        alert("Registering...", context);

                        message = "";
                        // await registerUser(user);
                        debugPrint(message);
                        if(message.contains("successful")){
                          debugPrint("in success....");
                          if(!mounted)return;
                          Navigator.pushNamed(context, "/signin");
                        }else{
                          debugPrint("Not success...");
                          if(!mounted)return;
                          alert(message, context);
                        }

                      }


                    },
                  ),
                ],
              ),
            )
          ],
        ),
      ),
    );
  }





}





