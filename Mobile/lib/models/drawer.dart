import 'package:rsdb/models/colors.dart';
import 'package:rsdb/models/text.dart';
import 'package:flutter/material.dart';

class CustomDrawer extends StatefulWidget {
  const CustomDrawer({Key? key}) : super(key: key);

  @override
  State<CustomDrawer> createState() => _CustomDrawerState();
}

class _CustomDrawerState extends State<CustomDrawer> {

  @override
  void initState() {
    // context.read<UserProvider>().provideUser();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return ListView(
      children: <Widget>[
        Container(
            width: MediaQuery.of(context).size.width,
            color: bgColor,
            child: const Center(
                child: Text("RSDB",
                    style: TextStyle(
                        fontWeight: FontWeight.bold,
                        fontSize: 18.0,
                        color: Colors.white)))),
        const Divider(
          thickness: 2.0,
          height: 2.0,
        ),
        Padding(
          padding: const EdgeInsets.only(top: 15.0, right: 10.0),
          child: ListTile(
            leading: const CircleAvatar(
              backgroundColor: bgColor,
              radius: 25.0,
              child: Icon(
                Icons.person_outline,
                size: 25.0,
                color: muteIconColor,
              ),
            ),
            title: text("userFirstName", textColor, size: 15.0),
            subtitle: text("userEmail",muteTextColor,size: 9.0),
            onTap: () {
              Navigator.popAndPushNamed(context, "/profile");
            },
          ),
        ),
        GestureDetector(
            onTap: (){
              Navigator.popAndPushNamed(context, "/profile");
            },
            child: text("My Profile", pink, size: 12.0)),
        const Divider(
          thickness: 1.0,
        ),
        const SizedBox(
          height: 10.0,
        ),
        drawerTile(Icons.view_comfy, "", "Notification"),
        drawerTile(Icons.email, "", "Email"),
        drawerTile(Icons.contact_support, "", "Contact"),
        drawerTile(Icons.contact_support, "", "About"),
        drawerTile(Icons.logout, "", "Logout"),
        drawerTile(Icons.view_comfy, "", "Version"),
      ],
    );
  }

  Widget drawerTile(IconData? icon, String route, String name, {Widget? subtitle} ){
    return ListTile(
        onTap: () {
          Navigator.pushNamed(context, route);
        },
        leading: Icon(
          icon,
          color: iconColor,
          size: 20.0,
        ),
        title: Text(
          name,
          style: const TextStyle(color: pink),
        ),
        subtitle: subtitle
    );
  }

}
