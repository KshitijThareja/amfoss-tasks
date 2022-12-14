import 'dart:ui';

import 'package:flame/game.dart';
import 'bunny_player.dart';
import 'bunny_world.dart';
import 'helpers/directions.dart';

class BunnyGame extends FlameGame {
  // ignore: prefer_final_fields
  BunnyPlayer _bunnyPlayer = BunnyPlayer();
  // ignore: prefer_final_fields
  BunnyWorld _bunnyWorld = BunnyWorld();
  @override
  Future<void> onLoad() async {
    super.onLoad();
    await add(_bunnyWorld);
    await add(_bunnyPlayer);
    _bunnyPlayer.position = _bunnyWorld.size / 1.5;
    camera.followComponent(_bunnyPlayer,
        worldBounds:
            Rect.fromLTRB(0, 0, _bunnyWorld.size.x, _bunnyWorld.size.y));
  }

  onArrowKeyChanged(Direction direction) {
    _bunnyPlayer.direction = direction;
  }
}
