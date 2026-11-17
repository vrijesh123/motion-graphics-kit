# 3D motion graphics ref — AiTelly, "Oreshnik hypersonic missile: how it works" (YouTube, local file)

Source URL not recorded (supplied as a local file that came through a downloader site; see `meta.json`).
9:08 (547.8 s), 1920×1080 landscape, 25 fps, 48 shots. Analysed 2026-11-17 chunk by chunk from
`chunks/part-01…09` (index in `chunks.json`). All times below are positions in the full video.

We borrow the explainer grammar only: sets, camera, materials, labels, pacing. The subject (a real weapon),
the narration's claims, the channel's watermark and its models are not ours and are not reused.

## Overview
- **What it is:** a long-form 3D technical explainer by the YouTube channel AiTelly (name from the watermark). It
  tells one object's story: what it is, its parts, how it flies, why it is hard to stop, and how it compares
  with a second object.
- **Structure:**
  1. A 68 s cold open that runs the whole story in miniature.
  2. Specs (weight, range, payload).
  3. The launch vehicle and how a cold launch works.
  4. The re-entry vehicle's anatomy, part by part.
  5. The flight sequence.
  6. Why it is hard to intercept, as one 88 s continuous diagram.
  7. A side-by-side comparison with a second missile on trajectory, speed, range and purpose.
  8. A plug for the channel's next video, with no end card.
- **Narration:**
  - 1,381 words in 547.8 s, or 2.5 words/s. Speech fills 83% of the runtime and is English (Whisper probability 1.0).
  - A steady, formal explainer read in which every sentence names what is on screen at that moment: one picture per sentence.
  - Whisper mishears the names ("Orishnig", "Iskandar"); the words are in `vo_words.json`.
- **Sound:** −18 LUFS. The tempo estimate is meaningless (confidence 0.08), and the audio was not listened to,
  so the voice's character and whether there is a music bed are unknown.

## Look
**Render:** real-time, game-engine look: simple PBR materials, fog for depth, no depth of field, little motion
blur except deliberate speed streaks. Secondary objects (cities, targets) are untextured white "clay"; props such
as trees are low-poly. Clean and readable rather than cinematic.

**One backdrop "set" per kind of idea** (colours measured from frames):

| Set | Colours | Used for |
|---|---|---|
| Teal studio | radial gradient, centre `#A2DECA`, mid `#6A9393`, edges `#435A5A` | exploded view of the whole object |
| Navy studio | radial gradient, centre `#005B89`, edges `#003272` | anatomy of one part (cut-aways, turntables) |
| Grey diagram world | flat `#87888D` floor and sky, white "+" grid markers, soft horizon band | trajectories, interception (one continuous take) |
| Flat grey card | `#88919B` | quick line diagrams with white bracket labels |
| Space | `#0D0E11` with sparse stars and soft nebulae | flight, separation, re-entry |
| Orbit over Earth | realistic Earth (clouds, city lights) or a stylised deep-blue one | range, phases, deployment |
| Flat-shaded globe | ocean `#5E85B6`, pale green land, range disc `#FCDE60` at ~60% opacity | range circles |
| Stylised map | coral land `#FE715C`/`#FD654B`, teal sea `#005E72`, neighbour cyan `#28FEFF` | where things are, attack paths |
| Daylight sandbox | grey-green ground with a white grid, rows of simple trees, flat sky | vehicles and launch mechanics |
| Blue-grey / periwinkle sandbox | sky `#6A87AD`, ground `#748791`; periwinkle `#95A5D2` with white grid lines | side-by-side comparisons, speed |
| Lavender top-down grid | `#7D8CB2` with white "+" markers | targets and impacts from above |
| Brown stage | floor `#584F44`, black sky band, light beams from below | the final face-off of two objects |
| Misty forest at dusk | fog centre `#404753`, dark vignette `#272B2F`, red-brown soil | "real world" launch scenes |

**Materials do the pointing** (each swap marks what the sentence is about):
- solid (normal);
- white X-ray wireframe, so a payload stays visible inside its vehicle;
- translucent ghost, to show the insides in flight;
- solid red on the one part being named; solid blue on a group of parts (all twelve wheels);
- cyan glass/hologram for an abstract or secret object (the "bus", a cruise missile);
- an animated glowing core, gold to orange-red, for "energy" inside a cut-away;
- a yellow wireframe grid scanning down a part, as a highlight.

**Labels, five kinds** (more than it needs; see "Avoid"):
1. **Key word as big 3D type in the scene:** lemon `#FEFD24`, bold humanist sans, all caps. It sits in world space, so it
   moves with the camera and sometimes lies in perspective on the ground. Acronyms are set very wide ("M I R V"),
   with a small full-name subtitle under them.
2. **Part tag:** amber box (`#F5B711`–`#FDC200`) with near-black `#120B0A` caps, joined to the part by a thin
   leader line that ends in a small dot. Small, about 14–20 px at 1080p.
3. **Top-left caption box:** the same amber, holding a stat or a summary line ("ability to maneuver").
4. **Thin white labels with bracket leaders** on the flat grey diagrams.
5. **White labels:** bold caps on dark scenes ("speed = Mach 11"), and place names as white 3D type lying on a map or
   globe surface.

The channel's logo watermark sits bottom right the whole time. It is theirs: never copy it.

## Chunk by chunk

### Part 01 · 0:00–1:08 · cold open: the whole story in a minute
| Time | Narration (gist) | Set | On screen | Camera | Out |
|---|---|---|---|---|---|
| 0.0–4.0 | names the object and its truck | misty forest | hero missile hovers above the ground, stages colour-coded; white 3D title stands in the scene | locked wide, slight drift | title fades 3.6–4.3 |
| 4.0–7.3 | "launched from a 12×12 truck" | forest | truck appears around the missile as a white X-ray wireframe, then turns solid (5.0–5.6); "12 X 12 TRUCK" types onto the ground in perspective | static | soft change |
| 7.3–12.9 | multiple stages, reaches orbit | forest | launcher erect, launch | low angle, tilting up | cut |
| 12.9–29.2 | hypersonic dive, fairing opens, six warheads | space; a stylised planet rim (pale teal, green edge) at 18 s | stage burn, fairing with speed streaks, bus opens; amber callout "6 WARHEADS" with leader | tracking beside the object | cuts at 20.5, 29.2 |
| 29.2–33.2 | thrusters on each warhead | day sky (`#5976B2` top) | warheads streak down with cyan plasma trails and orange nose heat | wide, diagonal crossings | cut |
| 33.2–38.4 | thrusters let them manoeuvre under gravity | white cloud fog | warhead close-up; pink-red arrows for thrust; yellow words build letter by letter | close, slow push | cut |
| 38.4–44.8 | almost impossible to hit | flat grey `#88919B` | two weaving yellow/green paths; white bracket labels for the two objects | slow tilt up along the paths; labels fade | low-contrast cut |
| 44.8–68.3 | three stages, solid fuel, six warheads | teal studio | **exploded view**: missile slides out of its canister, stages separate, fuel-cell icon (blue/red), big lemon words "1 STAGE · SOLID FUEL · 2 STAGES · 3 STAGES · 6 WARHEADS"; nose fairing opens like a clamshell and closes; yellow grid scans down the nose (63.3–64) | booms up and down the missile; the words travel with the scene | cut |

Takeaway: the open shows every set the video will use, so the viewer learns the visual vocabulary up front.

### Part 02 · 1:08–2:15 · specs, then the launch vehicle
| Time | Narration (gist) | Set | On screen | Camera | Out |
|---|---|---|---|---|---|
| 68.3–76 | weight at launch, payload weight | low orbit over a realistic Earth | amber top-left caption (words fade in left to right); small yellow "1.3 T" beside the payload | slow glide over the planet | – |
| 76–82.4 | range covers a continent | higher orbit | glowing green arcs draw from the launch area to red-glow targets; white bracket place label; big yellow range numbers bottom left | slow push/orbit | cut |
| 82.4–95.1 | carries independently targeted warheads | space over the limb | half-lit bus; "M I R V" letters pop one at a time (~0.3 s apart), full name in small type below | slow tilt down, Earth rises into frame | cut |
| 95.1–105.6 | origin of the design, much is classified | Earth close-up | country name as white 3D type lying on the globe; bus in blue holographic material; amber caption top right | slow orbit | cut |
| 105.6–134.5 | 12×12 platform, cold launch, compressed gas, engine ignites | daylight sandbox | truck on a slow turntable; wheels switch instantly to solid blue, then an amber "12x12 WHEEL" tag; launcher erects; "COLD LAUNCH SYSTEM" tag; canister cut-away with a violet glowing gas column; missile pops out, cap and base plate fall away, "ROCKET ENGINE IGNITES" | slow orbit, then low angle tilting up with the missile | cut |

### Part 03 · 2:15–3:21 · launch details and the warhead's anatomy
| Time | Narration (gist) | Set | On screen | Camera | Out |
|---|---|---|---|---|---|
| 134.5–159.6 | hot launch contrast, less wear, hydraulics | sandbox | a box launcher with an amber "HOT LAUNCH" tag; low-angle close-ups against clouds; back to the truck: canister close-up, "ADVANCED HYDRAULICS" tag, canister lowers and rises | moves between several setups **inside one shot** | cut |
| 159.6–168.0 | secure command links, coordinated fire | coral map | country name in white 3D type on the map; tiny launcher in the middle; dotted white arrows grow outwards (~1 s) to green dots | slow drift and rotation over the map | cut |
| 168.0–182.2 | fuse, nose, contact sensor, arming system | space | re-entry vehicles in formation (white cones, black bands); each named part turns solid red as its amber tag appears | side-on tracking, slow | cut |
| 182.2–188.1 | detonates at the right moment | lavender top-down grid | red crosshairs, falling vehicle, orange volumetric fireball, white X markers | top-down, static | cut |
| 188.1–201.0 | the warhead compartment | navy studio | cut-away: speckled green compartment lifts out of the shell (~0.6 s), turns red, "WARHEAD" tag; amber caption top left | static, slight drift | cut |

### Part 04 · 3:21–4:26 · manoeuvring, guidance, then the flight sequence begins
| Time | Narration (gist) | Set | On screen | Camera | Out |
|---|---|---|---|---|---|
| 201.0–209.0 | can manoeuvre at extreme speed | bright cloud deck, then vertical streaked clouds | vehicle trailing a glowing yellow path line; amber caption top left | tracking, then looking down the dive with vertical motion streaks | cuts |
| 209.0–222.0 | spin nozzles, spin gas generator | navy studio | the base turns towards camera; each named part turns red with its tag | the object turns, the camera holds | cut |
| 222.0–230.4 | guidance, satellite antenna | flat blue-grey sky | vehicle falling nose-down towards camera; antenna tag | static | cut |
| 230.4–233.4 | satellite navigation | space | satellite, dotted signal line, yellow "wifi" arcs at both ends | static | cut |
| 233.4–236.8 | reaches its destination | white clay city from above | fireball among the blocks | static aerial | cut |
| 236.8–266.4 | stage 1 boost, separation at ~60 s, shroud off, bus detaches at ~180 s | forest launch site, smoke, then space | cold launch, ignition, huge smoke plume; **the missile climbs into its own smoke, which fills the frame (255.2–255.8) and hides the cut**; stage burn in space; the bus in cyan glass with a white quoted caption | low-angle chase | cut |

### Part 05 · 4:26–5:03 · deployment and re-entry
| Time | Narration (gist) | Set | On screen | Camera | Out |
|---|---|---|---|---|---|
| 266.4–276.4 | bus moves into position, releases the vehicles | high orbit over a cloudy Earth | shroud halves part; bus with dish releases the vehicles | slow orbit and rise: the Earth climbs into frame and **the sun's highlight sweeps across the object** | cut |
| 276.4–280.8 | very high parabolic path | space over the limb | a thin white arc draws upwards from the horizon into a full parabola (~1.5 s) | static wide | cut |
| 280.8–294.8 | falls at about Mach 11, rotating thrusters steer | Earth below | close-ups of the vehicle; white bold speed label; small yellow thruster jets fire from the base | side tracking, closer | cut |
| 294.8–303.2 | air burst or ground burst | space | cut-away warhead with an animated glowing core (gold to orange-red); grey part label; white two-line label typed letter by letter | static, slight push | cut |

### Part 06 · 5:03–6:31 · why it is hard to intercept (one continuous 88 s take)
No hard cut. The camera flies between setups inside one grey diagram world.

| Time | Narration (gist) | On screen | Camera |
|---|---|---|---|
| 303.2–313 | speed decides everything | missile in flight; at ~307 it turns translucent (X-ray) and back | side tracking |
| 313–329 | climbs high, then dives; seconds matter | launch; the missile **draws a thick yellow ribbon (`#F5DD45`) behind it** as it climbs, arcs over and flies level | chase camera keeps the missile centred |
| 329–341 | "the longer shot": the parabolic trajectory | **pull back over ~2 s (328.8–330.6) until the whole flight profile shows as a thin line**: wiggly boost, high arc, weaving end; small amber tags on the curve | fast ease-in-out pull-back, no cut |
| 341–357 | gains kinetic energy, can wriggle mid-flight | vehicles scatter at the apex; big tilted amber "KINETIC ENERGY" tag in 3D; camera flies along the line and back out | flies along the path |
| 357–391 | interceptor can't track a zig-zag at that speed | interceptor launches inside a green translucent cone (its tracking envelope) with an amber tag; red and green paths weave; a miss, small fireball on the ground at ~389 | tracking, then wide |

Takeaway: one world plus one camera explains a process better than cuts. The ribbon is real 3D geometry,
thick close up and a hairline from far away, so the pull-back itself shows the scale.

### Part 07 · 6:31–7:38 · comparison: trajectory and speed
| Time | Narration (gist) | Set | On screen | Camera | Out |
|---|---|---|---|---|---|
| 391.2–401.2 | compare the two on trajectory, speed, range, purpose | blue-grey sandbox | small green launcher beside the big black one, yellow 3D names with bracket underlines; a stacked yellow list builds on the left as each word is said | pull-back | cut |
| 401.2–404.7 | quasi-ballistic trajectory | space over Earth | thin green path with an arrowhead draws on; yellow title types across the top | static | cut |
| 404.7–408.4 | part ballistic, part cruise | grey-blue floor, black sky | three missiles side by side in three materials: white X-ray, solid with an orange gradient (the hybrid), cyan hologram | static | cut |
| 408.4–416.8 | manoeuvres unpredictably mid-flight | flat grey sky | two horizontal paths, wavy against straight; yellow labels typed under each | slow pan following | cut |
| 416.8–423.6 | flies low, under conventional defences | dark sky, khaki ground | concentric orange radar rings; white dashed high and low paths; white label on the ground | static | cut |
| 423.6–448.8 | three phases: boost, mid-course, terminal | Earth from space (stylised blue) | thin yellow arc with "1/2/3 PHASE"; **each phase name fills the screen in huge lemon type, typed at ~10 letters/s**, as the camera rides the arc; then all three shrink into a labelled overview | rides the arc, then pulls back | cut |
| 448.8–458.4 | both reach hypersonic speed | horizontal grey speed-streak tunnel, then a green field with white lines | side-on missiles with amber name tags; big lemon speed figure lying over the field | side tracking | cut |

### Part 08 · 7:38–8:34 · comparison: interception, speed, range
| Time | Narration (gist) | Set | On screen | Camera | Out |
|---|---|---|---|---|---|
| 458.4–466.6 | difficult to intercept | grey planet surface under a translucent teal defence dome | arcs for the vehicle and two interceptors; yellow speed label; amber tags | slow push | cut |
| 466.6–476.5 | the second missile's speed range | periwinkle set with white grid lines | green missile with its name as white 3D type beneath it; white 3D speed range in perspective, built from letter fragments; then a grey cloud shot with a "key distinction" tag | side tracking | cut |
| 476.5–481.3 | long-range missiles | green hills with a white grid | erect launcher; amber caption top left | low angle | cut |
| 481.3–491.4 | range over 5,500 km | flat-shaded globe | yellow translucent range disc grows from the launch point; red arcs; small dark km/miles text inside the disc | push in, then pull back to the whole globe | cut |
| 491.4–502.6 | the second missile's 500–700 km | periwinkle flat set | launch, thin arc draws, yellow km/miles numbers | wide static | cut |
| 502.6–514.1 | purpose separates them | brown stage | the two missiles stand side by side, light beams shining up from the floor, amber name tags | slow push in | cut |

### Part 09 · 8:34–9:08 · purpose, then the plug
| Time | Narration (gist) | Set | On screen | Camera | Out |
|---|---|---|---|---|---|
| 514.1–525.8 | strategic weapon, critical infrastructure | space over a brown planet, then top-down brown ground | vehicle approaching; top-down target board of clay city blocks, an industrial site and a green airfield; black circles converge; white place labels build letter by letter | static, top-down | cut |
| 525.8–541.4 | the other is tactical, for battlefield targets | coral map with a cyan neighbour | green missiles cross the border; vehicles and buildings hit by small explosions | slow pan and push over the map | cut |
| 541.4–547.8 | plug for another video, subscribe | grey cloud | teaser shot from the channel's next video; **no end card** | slow push | end |

## Motion language
- **Cutting:**
  - Hard cuts on sentence boundaries; shots run 3–25 s, about 11 s on average.
  - Inside long shots the camera moves between setups instead of cutting (134–160 s, and all of part 06).
- **Transitions:**
  - Mostly hard cuts.
  - A pass-through occlusion, where the camera climbs into smoke and the cut hides behind it (255 s).
  - A reveal by pulling back (329 s).
  - A title fade (4 s).
  - Low-contrast cuts between similar greys (44.8 s).
- **Camera:**
  - Slow drifts and orbits most of the time.
  - Chase and tracking alongside objects in flight.
  - Low angles tilting up for launches.
  - A fast ease-in-out pull-back (~2 s) to reveal a whole path; riding along a trajectory.
  - Top-down for maps and targets.
  - No shake, no depth of field.
- **Objects:**
  - Exploded views: parts slide apart in ~0.6 s, hold, slide back.
  - Turntables; clamshell open and close.
  - Highlight swaps are **instant**, with no fade.
- **Text:**
  - 3D key words build in and out as letter fragments (~0.35 s).
  - Big phase names and white labels type on at ~10 letters/s.
  - Wide-set acronyms pop one letter at a time (~0.3 s apart).
  - Tags: the amber bar wipes in, then the text appears (~0.3 s).
  - Top-left captions: the box pops, then the words fade in left to right (~0.4 s).
  - A label leaves when the next part is named.
- **Diagram lines:**
  - Trajectories are ribbons drawn on behind the moving object.
  - Arcs draw up from the horizon in 1–1.5 s; dotted arrows grow outwards in ~1 s.
  - Radar rings expand; range discs grow from a point.
- **Pacing:** something new every 4–8 s even inside a long shot (a label, a part, a new camera setup); every
  sentence gets its own picture.

## Borrow / avoid
**Borrow:**
- One set per kind of idea, so the backdrop alone says "anatomy" or "flight" or "comparison".
- Material swaps to point: red part, X-ray, ghost, scan.
- Exploded views with a tag per part.
- The key word as big 3D type living in the scene.
- Paths drawn as 3D ribbons.
- One continuous camera to explain a process.
- Occlusion transitions.
- Side-by-side comparisons on a neutral stage.

**Avoid:**
- Five label styles and two yellows.
- Misspelled on-screen words ("TRAGETABLE", "ISKANDAR").
- Labels too small for a phone.
- A watermark competing with the labels.
- Low-poly trees and flat lighting, which look cheap.
- 16:9 framing: our kit makes 1080×1920.

## Recreate-it notes (HyperFrames + Three.js, 1080×1920)
Read `/hyperframes` `references/types/3d.md` and `references/runtimes.md` first. Draw every frame from `hf-seek`
time, with no `requestAnimationFrame` loop and seeded randomness. Precompute paths and any simulation at load.

- **Studio sets:**
  - Render with a transparent clear colour over a CSS gradient on the page:
    - teal studio: `radial-gradient(ellipse 70% 55% at 50% 45%, #A2DECA 0%, #6A9393 50%, #435A5A 100%)`;
    - navy studio: `radial-gradient(ellipse 70% 55% at 50% 45%, #005B89 0%, #003272 100%)`.
  - Diagram world: background `#87888D`, a ground plane with small "+" sprites about every world unit, and fog
    (`THREE.Fog(0x87888D, near, far)`) so the grid fades out before the horizon.
- **Lighting:** the reference is flat, ambient-heavy studio light. Do better with 3d.md's recipe: warm key, cool rim, an
  environment with soft strips, and a contact shadow under the object.
- **Highlight swap:**
  - Keep two materials per part and switch `mesh.material` when `t >= tHighlight`; that is the reference's instant swap.
  - An emissive ramp over 0.15 s reads smoother and still feels decisive.
- **X-ray to solid:** draw `EdgesGeometry` as white `LineSegments` (opacity ~0.7) over the mesh, then fade the solid
  material's opacity 0 → 1 and the lines 0.7 → 0 over 0.6 s.
- **Scan:** a yellow wireframe copy of the part, revealed by a clipping plane that moves along the part's axis over
  ~0.8 s.
- **Exploded view:** tween parts along their axis for ~0.6 s with `power2.inOut`, opening gaps of about 30–40% of a
  part's length. Hold at least 1.5 s with the part's tag, then close.
- **Part tags:**
  - HTML overlay placed each seek by projecting the anchor's world position (`anchor.clone().project(camera)`).
  - Box in the accent colour with dark caps, 2 px leader line, 8 px dot on the part.
  - Animate the bar `scaleX` 0 → 1 over 0.25 s, then fade the text in over 0.15 s.
  - At 1080 wide, tags need ≥ 28 px text (kit rule), about twice the reference's size.
- **Big 3D words:**
  - In-world text (for example troika-three-text with the project font) placed beside the object, so camera moves carry it.
  - Fragment build: split into letters, give each a seeded random delay of 0–0.2 s and an opacity/clip reveal of
    0.15 s, about 0.35 s for the word.
- **Trajectory ribbon:**
  - Build a `CatmullRomCurve3` at load, then a `TubeGeometry` with a world-space radius, so it thins as the camera pulls back.
  - Reveal it with `geometry.setDrawRange(0, Math.floor(indexCount * progress))`, where progress comes from the object's position at time `t`.
- **Pull-back reveal:** 2.0 s, `power2.inOut`, from ~3 object lengths away to the whole path in frame. Keep the
  object in frame throughout.
- **Occlusion transition:** a smoke or cloud layer in front of the camera covers the frame completely for ≥ 0.3 s,
  and the cut happens under it.
- **Vertical framing:**
  - Tall subjects (rockets, towers, a phone, a server rack) fill 1080×1920 naturally; put tags left and right of the object and big words above or below it.
  - A 25–60 s reel has room for 3–5 ideas: one set each, one camera move per shot, a new visual every 3–5 s.
- **Brand mapping:** swap the reference's teal/amber/lemon for the client's palette. For a WOLFx "how it works"
  piece:
  - a light-grey or white studio;
  - the part highlight in WOLFx red;
  - tags as black boxes with white Poppins;
  - see `clients/wolfx/brand.md`.

## Not verified
- The audio was not listened to: the voice's character and whether there is music are unknown.
- The render engine and font names are guesses from the look.
- Colours are medians of compressed-video pixels, so they may be off by a few levels.
- Each chunk was viewed at one frame every 2 s plus bursts at 0.2–0.6 s steps, so brief events between samples may be missed.
- The narration's factual claims were not checked and are not for reuse.
