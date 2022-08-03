import 'package:flutter/material.dart';
import 'package:rsdb/models/colors.dart';


class AcknowledgeButton extends StatelessWidget {
  final String name;
  final void Function()? onPressed;
  const AcknowledgeButton({required this.name, this.onPressed, Key? key})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(left: 15.0, right: 15.0, bottom: 15.0),
      child: Material(
          elevation: 5.0,
          borderRadius: BorderRadius.circular(18.0),
          color: bgColor,
          child: SizedBox(
            height: 50.0,
            width: 280.0,
            child: MaterialButton(
              minWidth: MediaQuery.of(context).size.width,
              // padding: EdgeInsets.fromLTRB(20.0, 15.0, 20.0, 15.0),
              onPressed: onPressed,
              child: Text(
                name,
                textAlign: TextAlign.center,
                style:
                const TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
              ),
            ),
          )),
    );
  }
}


class DeclineButton extends StatelessWidget {
  final String name;
  final void Function()? onPressed;
  const DeclineButton({required this.name, this.onPressed, Key? key})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(left: 15.0, right: 15.0, bottom: 15.0),
      child: Material(
        child: SizedBox(
          height: 50.0,
          width: 280.0,
          child: MaterialButton(
            minWidth: MediaQuery.of(context).size.width,
            shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(18.0),
                side: const BorderSide(color: bgColor)),
            onPressed: onPressed,
            child: Text(
              name,
              textAlign: TextAlign.center,
              style: const TextStyle(color: bgColor, fontWeight: FontWeight.bold),
            ),
          ),
        ),
      ),
    );
  }
}


class HalfDeclineButton extends StatelessWidget {
  final String name;
  final Color color;
  final BuildContext? context;
  final void Function()? onPressed;
  const HalfDeclineButton(
      {this.context,
        required this.name,
        required this.color,
        this.onPressed,
        Key? key})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Material(
        child: SizedBox(
          width: 140.0,
          height: 40.0,
          child: MaterialButton(
            minWidth: (MediaQuery.of(context).size.width / 4) - 10,
            shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(18.0),
                side: BorderSide(color: color)),
            onPressed: onPressed,
            child: Text(
              name,
              textAlign: TextAlign.center,
              style: const TextStyle(color: bgColor, fontWeight: FontWeight.bold),
            ),
          ),
        ));
  }
}



