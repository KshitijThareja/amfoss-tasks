// ignore_for_file: empty_statements

import 'package:flame/game.dart';
import 'package:flamegame/helpers/navigation_keys.dart';
import 'package:flutter/material.dart';
// ignore: unused_import
import 'package:flame/flame.dart';
// ignore: unused_import
import 'bunny_game.dart';

void main() {
  final game = BunnyGame();
  runApp(
    MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        body: Stack(
          children: [
            GameWidget(
              game: game,
            ),
            Align(
              alignment: Alignment.bottomRight,
              child: NavigationKeys(
                onDirectionChanged: game.onArrowKeyChanged,
              ),
            ),
          ],
        ),
      ),
    ),
  );
}
