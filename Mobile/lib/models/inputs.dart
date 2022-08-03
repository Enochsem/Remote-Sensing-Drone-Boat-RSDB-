import 'package:flutter/material.dart';
import 'package:rsdb/models/colors.dart';


class FullInput extends StatelessWidget {
  final bool? expands;
  final TextEditingController? controller;
  final String? initialValue;
  final String? label;
  final String? hint;
  final bool obscureText;
  final TextInputType? keyboardType;
  final Icon? prefixIcon;
  final String? Function(String?)? validator;
  final void Function(String?)? onSaved;
  final void Function(String)? onChanged;
  const FullInput({
    this.expands,
    this.label,
    this.controller,
    this.initialValue,
    this.hint,
    required this.obscureText,
    this.keyboardType,
    this.prefixIcon,
    this.validator,
    this.onSaved,
    this.onChanged,
    Key? key
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.only(left: 15.0,right: 15.0, bottom: 15),
      width: MediaQuery.of(context).size.width,
      child: TextFormField(
        initialValue: initialValue,
        controller: controller,
        obscureText: obscureText,
        keyboardType: keyboardType,
        validator: validator,
        onSaved: onSaved,
        onChanged: onChanged,
        decoration: InputDecoration(
          prefixIcon: prefixIcon,
          border: const OutlineInputBorder(),
          labelText: label,
          hintText: hint,
        ),
      ),
    );
  }
}




class HalfInput extends StatelessWidget {
  final TextEditingController? controller;
  final String? initialValue;
  final String? label;
  final String? hint;
  final bool obscureText;
  final TextInputType? keyboardType;
  final Icon? prefixIcon;
  final void Function()? onTap;
  final String? Function(String?)? validator;
  final void Function(String?)? onSaved;
  final void Function(String)? onChanged;
  const HalfInput({
    this.label,
    this.controller,
    this.initialValue,
    this.hint,
    required this.obscureText,
    this.keyboardType,
    this.prefixIcon,
    this.onTap,
    this.validator,
    this.onSaved,
    this.onChanged,
    Key? key
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.only(left: 15.0,right: 15.0, bottom: 15.0),
      width: (MediaQuery.of(context).size.width/2)-5,
      child: TextFormField(
        controller: controller,
        initialValue: initialValue,
        obscureText: obscureText,
        keyboardType: keyboardType,
        onTap: onTap,
        validator: validator,
        onSaved: onSaved,
        onChanged: onChanged,
        decoration: InputDecoration(
          prefixIcon: prefixIcon,
          border:  OutlineInputBorder(
              borderSide: BorderSide(color: halfInputOutlineColor)
          ),
          labelText: label,
          hintText: hint,
        ),
      ),
    );
  }
}
