// Future<bool> signInUser(SignIn user) async {
//   var body = {"email": user.email, "password": user.password};
//   var url = Uri.parse("$baseURL/user/login");
//   try {
//     // debugPrint("sign body $body \n ${json.encode(body)}");
//     var response = await http.post(url, body: body);
//     debugPrint('sign in status: ${response.statusCode}');
//     if (response.statusCode == 200) {
//       var userResponse = jsonDecode(response.body);
//       // debugPrint("TOKEN FROM SIGN IN ${userResponse['jwtToken']}");
//
//       sp.setBoolKeyValue("isVerified",userResponse['isVerified']);
//       sp.setKeyValue("txLimit",userResponse['txLimit']);
//
//       sp.setToken(userResponse['jwtToken']); //get and store token in SP
//       sp.setKeyValue("email", userResponse['email']);
//       sp.setKeyValue("password", user.password);
//       // print("sp email in sign in ${await sp.getValue("email")} ");
//       DataBaseHelper.instance.insertUser( SignIn.dbUserObject(userResponse, user.password));
//       return true;
//     }else{return false;}
//   } on HttpException {
//     // print("error could not find post");
//     throw Exception(HttpException);
//   } on SocketException {
//     // print("no internet connection");
//     throw Exception(SocketException);
//   } on FormatException {
//     // print("bad response format");
//     throw Exception(FormatException);
//   }
//   // throw Exception("Sorry an Error Occurred");
// }
