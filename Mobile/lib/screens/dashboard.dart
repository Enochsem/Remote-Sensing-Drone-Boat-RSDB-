import 'package:flutter/material.dart';

class Dashboard extends StatefulWidget {
  const Dashboard({Key? key}) : super(key: key);

  @override
  State<Dashboard> createState() => _DashboardState();
}

class _DashboardState extends State<Dashboard> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: ListView.builder(
        itemCount: 4,
        itemBuilder: (context, index){
          return const SizedBox(
            child: Card(
              child: ListTile(
                title: Text("PH SENSOR"),
                subtitle: Text("8.0ph"),
                trailing: Icon(Icons.sensors_outlined),
              ),
            ),
          );
        },
      )
    );
  }
}
