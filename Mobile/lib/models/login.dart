

class User{
  String? user_id;
  String? device_id;
  String? password;
  String? confirmPassword;

  User({
    this.user_id,
    this.device_id,
    this.password,
    this.confirmPassword
  });


  factory User.getRegisteredUser(Map<String, dynamic> user) {
    return User(
        device_id: user["email"],
        password: user["password"],
        confirmPassword: user["confirmPassword"],
        );
  }


}