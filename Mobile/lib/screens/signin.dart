import 'package:flutter/material.dart';
import 'package:rsdb/models/login.dart';
import 'package:rsdb/models/inputs.dart';
import 'package:rsdb/models/buttons.dart';
import 'package:rsdb/models/colors.dart';
import 'package:rsdb/models/text.dart';

import 'dart:io';

class Login extends StatefulWidget {
  const Login({Key? key}) : super(key: key);

  @override
  State<Login> createState() => _LoginState();
}

class _LoginState extends State<Login> {
  final _formKey = GlobalKey<FormState>();
  final User _user =  User();
  bool validUser = false;

  TextEditingController usernameController = TextEditingController();
  TextEditingController passwordController = TextEditingController();

  // check internet access
  bool isOnline = false;

  Future<void> checkConnection() async {
    try {
      final result = await InternetAddress.lookup('google.com');
      if (result.isNotEmpty && result[0].rawAddress.isNotEmpty) {
        setState(() {
          isOnline = true;
          // alert("Online", context);
          debugPrint('connected');
        });
      }
    } on SocketException catch (_) {
      setState(() {
        isOnline = false;
        alert("You are Offline", context, color: pink);
        debugPrint('not connected');
      });
    }
  }

  @override
  void initState() {
    checkConnection();
    super.initState();
  }

  @override
  void dispose() {
    usernameController.clear();
    passwordController.clear();
    super.dispose();
  }

  void temp() {
    usernameController.text = "";
    passwordController.text = "";
  }

  @override
  Widget build(BuildContext context) {
    // temp();
    return Scaffold(
      body: Container(
        padding: const EdgeInsets.fromLTRB(30, 15, 30, 15),
        child: ListView(
          padding: const EdgeInsets.all(10.0),
          children: [
            const SizedBox(
              height: 25.0,
            ),
            titleText("Sign in", size: 30.0),
            
            Image.asset(
              "images/drone.png",
              height: 300.0,
            ),
            Form(
              key: _formKey,
              child: Column(
                children: [
                  FullInput(
                    controller: usernameController,
                    obscureText: false,
                    label: 'Email',
                    hint: 'Enter User ID',
                    keyboardType: TextInputType.emailAddress,
                    validator: (value) {
                      if (value == null || value.isEmpty) {
                        return 'User ID is required';
                      }
                      _formKey.currentState?.save();
                      return null;
                    },
                    onSaved: (String? value) {
                      _user.user_id = value;
                    },
                  ),
                  FullInput(
                    controller: passwordController,
                    obscureText: true,
                    label: 'Password',
                    hint: 'Enter Password',
                    keyboardType: TextInputType.visiblePassword,
                    validator: (String? value) {
                      if (value == null || value.isEmpty) {
                        return 'Password is required';
                      }
                      _formKey.currentState?.save();
                      return null;
                    },
                    onSaved: (String? value) {
                      _user.password = value;
                    },
                  ),
                  AcknowledgeButton(
                    name: "Sign in",
                    onPressed: () async {
                      if (_formKey.currentState!.validate()) {
                        _formKey.currentState?.save();
                        validateSignIn(context);
                      }
                    },
                  ),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.start,
                    children: [
                      TextButton.icon(
                          onPressed: () {
                            Navigator.pushNamed(context, "/forgot");
                          },
                          label: const Text(
                            "forgot password?",
                            textAlign: TextAlign.left,
                          ),
                          icon: const Icon(Icons.lock)),
                    ],
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  Future<void> validateSignIn(BuildContext context) async {
    if (validUser == false) {
      alert("Processing", context);
    }
    //Check if user exists in the database and validate using that data once the user has log in before
    var dbUser = [];
    // await DataBaseHelper.instance.getUser();
    if (isOnline) {
      validUser = true;
      // await signInUser(_user);
    } else {
      for (int i = 0; i < dbUser.length; i++) {
        if (dbUser[i] == _user.user_id &&
            dbUser[i] == _user.password) {
          validUser = true; //DB valid user
        }
      }
    }

    if (validUser) {
      if (!mounted) return;
      Navigator.pushNamedAndRemoveUntil(
          context, "/home", (Route<dynamic> route) => false);
    } else {
      if (!mounted) return;
      alert("Email or password is incorrect", context);
    }

    //  clear fields
    usernameController.text = "";
    passwordController.text = "";
  }

  void alert(String message, BuildContext context, {Color color = bgColor}) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        elevation: 0.0,
        behavior: SnackBarBehavior.floating,
        // margin: const EdgeInsets.only(bottom: 420.0),
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
}
