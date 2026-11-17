# SPEC: Lykos Wx-1 launch film (built from script.md, Draft 3)

GOAL:    the viewer remembers "Lykos Wx-1, engineered by WOLFx" and wolfx.io.
OUTPUT:  HyperFrames 0.9.19, 1080 x 1920, 30 fps, text only (no voice-over).
TIME:    v2: 52.8 s x 30 fps = 1584 frames, timed to the voice-over (MAP in index.html); designed on a 70 s grid.
LOOK:    v2 = WOLFx dark flip, bold: night #0B0B0B, grid #242424, contours #5E5E5E, gunmetal #3B3F44, white type,
         red #FF2B2B key words, orange flame. (v1 was the white wolfx.io page, as below.)
         - ground: pure white #FFFFFF floor and sky; grid #DCDCDC every 2 units; contour lines #909090, 1 px;
           white fog from 45 to 150 units.
         - dark flip: #121212 with a #2E2E2E grid.
         - studio: radial #FFFFFF to #E6E6E6.
         - ink #121212.
         - accent #FF2B2B, one element per shot, only on lines or words of 100 px and up.
         - type: Poppins SemiBold 64 px lead lines (-0.01em, left at 80 px, top 236 px, Title Case).
           Big 3D words in ExtraBold. Tags SemiBold 34 px. Pills Bold 42 px.
         - light: hemisphere 1.15, warm key 2.3 from upper left, cool rim 1.7 from behind right;
           contact shadows at 0.42 opacity.
OBJECTS: - Lykos: three stages, fins, a clamshell nose over seven pods (six around one), the "LYKOS Wx-1" stencil
           and the white Wx monogram (logo file, white).
         - 8x8 launcher: 4 axles, cab, erector rail on a pivot, two pistons.
         - launch tube; payload close-up with 4 thrusters; interception diagram (red payload path against a grey
           dashed interceptor path).
MOTION:  - ease-in-out cubic on camera keys; ease-out cubic on entrances; no bounce.
         - words step in 0.14-0.2 s apart (0.42 s each).
         - 3D words build from letter fragments in 0.18 s with up to 0.2 s seeded stagger.
         - tags: the bar wipes in 0.25 s, then the text appears in 0.15 s.
SHOTS:   0-6 hero | 6-12 X-ray launcher | 12-18 raise, ignite, lift-off into smoke | 18-28 space, stage drop, dive,
         nose opens | 28-32 seven trails | 32-38 thrusters | 38-46 diagram | 46-60 exploded view | 60-64 sign-off and
         lift-off | 64-70 end card (see script.md for every timing).
BANNED:  dark void with small floating objects (shots fill 40%+ of the frame); glow, bloom, lens flares;
         text drifting while it is read; text in the top 168 px or below 1330 px; explosions; real weapons,
         countries or defence systems; an extruded 3D wordmark (the logo is a PNG).
QA:      0.0 (missile on frame 0), 4.8 (lockup), 10.6 (label legible), 13.2 (missile under the text),
         17.9 (white-out), 25.5 (pods + tag), 30.4 (trails clear of text), 35.2 (word, payload, arrow),
         44.5 (diagram), 50.6 (Solid Fuel tag), 57.6 (payload words), 62.9 (pills), 69.75 (end card).
