# Stabi Runner — Final Candidate v2

Included:
- Wallet / Sepolia removed from the game and Shop.
- Official USDZ SVG used in HUD, collectibles and Shop.
- Collected USDZ is saved as **In-game USDZ Points** (not real USDZ tokens).
- Shop uses only in-game USDZ Points.
- Sword: consumable stock; every auto-slash consumes ×1.
- Shield: consumable stock; every automatic protection consumes ×1.
- Speed Boots: permanent upgrade; Dash duration increases automatically.
- Recovery Core: permanent upgrade; supports a true 4-life maximum throughout the run.
- My Items shows only owned content.
- Default Stabi, Cyber Stabi, and USDZ Stabi.
- USDZ Stabi uses the user's actual frames: Run 6 / Jump 3 / Slide 2 / Hurt 2 / Death 4 / Victory 2.
- Cyber animation remains included.
- Character is smaller on mobile.
- Mobile touch handling prevents browser double-tap interference.
- Early obstacle speed and spawn rate are more forgiving.
- Compact Menu keeps Pause unobstructed.
- Cinematic Phase 2 portal finish remains.
- Unified audio and X share/card remain.

In-game prices:
- Stability Sword: 5 USDZ Points each
- Zero-Slippage Shield: 8 each
- Speed Boots: 40
- Recovery Core: 60
- Cyber Stabi: 100
- USDZ Stabi: 150

Deploy all files in this ZIP to the repository root.

- v4 fix: restored ☰ MENU click/touch handler on mobile and desktop.

- v5 USDZ fix: collectible, HUD and Shop now use the official USDZ logo supplied by the user.
- Added `usdz-coin.png` rendered directly from the official SVG for reliable canvas/mobile display.
- Removed the old yellow-circle collectible fallback.

- v6 Shop Fix:
  - Equipment renders immediately when Shop opens.
  - Skins tab renders reliably.
  - Shop initializes only after DOM is ready.
  - Shop/My Items buttons remain inside compact Menu.
  - Mobile click/touch behavior improved.


## Desktop Mode Required
- Mobile layout is blocked below 900px CSS viewport width.
- Players on phones are instructed to enable **Desktop Site**.
- Recommended orientation: landscape.
- Game unlocks automatically once desktop-sized viewport is detected.

- Desktop gate fix: Android Chrome can keep a narrow CSS viewport even after Desktop Site is enabled.
- The player now enables Desktop Site, taps confirmation once, and the session unlocks normally.

## Skin Performance + Shield Fix
- Cyber/USDZ skin frames now lazy-load by animation state.
- Only RUN preloads when a skin is equipped.
- Jump/Slide/Hurt/Death/Victory load only when needed.
- Reduced mobile image smoothing load.
- Shield radius reduced from ~58% to ~42% of character size.
- Shield glow/burst intensity reduced for clearer gameplay.

## v7 Freeze Fix
- Skin frames are no longer embedded as multi-megabyte base64 strings inside JavaScript.
- Every Default/Cyber/USDZ animation frame is now a separate WebP file under `/skins/`.
- Only the animation state currently needed is decoded.
- Sword auto-slash no longer forces a synchronous DOM layout/reflow.
- Sword slash has a short cooldown and lighter particles.
- Sword activation range reduced slightly to avoid repeated heavy effects.

## v8 Asset Fallback Fix
- Removed the `/skins/` folder dependency.
- All skin WebP assets are now placed directly in the repository root.
- If a Cyber/USDZ frame fails to load, the game falls back to Default Stabi instead of showing nothing.
- Broken/not-yet-loaded frames are never drawn.
- Added a skin asset watchdog and startup fallback.
- IMPORTANT: upload every file from this ZIP, not only index.html.

## v9 Share to X Fix
- Score is now always converted to a real number.
- USDZ collected reads the numeric value, not the HTML span object.
- Prevents `NaN` and `[object HTMLSpanElement]` in X posts.

## v10 Sword Freeze Fix
- Rebuilt Stability Sword auto-slash as a canvas/game-loop-only mechanic.
- Removed DOM slash animation and `Element.animate()` from combat.
- Sword stock is decremented directly and safely.
- Destroyed MEV/Slippage is removed only after the lightweight slash check.
- Added a short 0.32s cooldown to avoid repeated processing.
- Sword stock HUD updates inside the normal game update loop.

## v11 Skin Visual Normalization
- Default Stabi is the 1.00 visual-size reference.
- Cyber states are normalized around 1.10–1.13.
- USDZ states are normalized around 1.11–1.14.
- Character visuals are centered horizontally and anchored by the feet.
- Collision/hitbox size is unchanged.
- Built on v10, so the Sword freeze fix and all previous Shop/USDZ fixes remain included.

## v12 Unique Sword Slash + HUD
- Sword stock is visible in gameplay as STABILITY SWORD ×N.
- Sword is auto-active; no Equip button is needed.
- Default Stabi: teal/white crescent slash + sparkles.
- Cyber Stabi: purple crescent + digital square particles.
- USDZ Stabi: golden crescent + USDZ-style `$` spark accents.
- One successful slash consumes exactly one Sword.
- Slash effect is canvas-only (~0.22 sec), avoiding the old DOM-animation freeze.
- Includes v11 Skin Normalization and v10 Sword Freeze Fix.

## v13 All Fixes Test Build
This build intentionally combines the requested systems so they can be bug-tested together.

- Live skin switching: no page refresh required.
- Skin is cosmetic only; core hitbox/combat/inventory are shared.
- Unified Sword/Shield inventory source independent of selected skin.
- Sword remains auto-active with stock visible in gameplay.
- Default/Cyber/USDZ visual scale tightened and Run cadence normalized.
- Enemy visuals redesigned while preserving original gameplay types:
  - red evil character = SLIPPAGE
  - purple evil character = MEV
  - large robot = MEV BOTS
  - triangular enemy = PRICE IMPACT
- Enemy labels remain visible.
- Added a small TEST BUILD HUD showing active skin and Sword/Shield stock.
- Includes unique per-skin slash effects from v12.

## v14 Shop Items Fix Test
- Sword logic left unchanged.
- Shield stock/HUD + visible canvas shield + block-consume path.
- Shoes stock/HUD + jump boost while owned.
- Extra Life stock/HUD + rescue path at zero lives.
- Includes v13 changes.

## v15 — 5000 SP / Consumables / Monsters
- Phase 2 finish target is now 5000 SP.
- Progress bar is calculated from SP: 2500 SP = 50%, 5000 SP = 100%.
- Difficulty increases across 5 SP tiers.
- Stability Sword remains on the working auto-slash logic.
- Shield is consumable: BUY ×1/×5/×10, each blocked hit consumes ×1.
- Speed Boots is consumable: BUY ×1/×5/×10, each manual Stability Dash consumes ×1.
- Recovery Core is consumable: BUY ×1/×5/×10, automatically revives Stabi when the final life is lost and consumes ×1.
- Gameplay HUD always shows stock for Sword / Shield / Boots / Core.
- Slippage, MEV, Price Impact and MEV Bots now use monster/evil-character canvas visuals while retaining their labels and original gameplay hitboxes.

## v15.1 Jump Fix
- Restored normal Jump and Double Jump.
- Removed stale dependency on the old `stabiJumpBoost()` helper.
- Speed Boots remain tied to Stability Dash only.
- Sword, slash effects, monsters, 5000 SP target, Shield and Recovery Core logic were not intentionally changed.

## v15.2 Monster Update
- Keeps the v15.1 jump/double-jump fix.
- Replaces simple enemy shapes with richer animated canvas characters:
  Slippage slime, MEV rogue, Price Impact spiked beast, and MEV Bot robot.
- Enemy names remain above their heads.
- Idle/movement animation uses bobbing, pulsing eyes/reactor, cloak/blade motion and slime motion.
- All four enemy types can now appear from the early part of a run; later SP tiers increase pressure.
- Existing 5000 SP goal and consumable shop systems are preserved.

## v15.3 Monster Renderer Fix
- Replaced the actual `drawEntity(e)` enemy branches instead of adding a competing renderer.
- Old red/purple boxes and old triangle obstacle are no longer used for Slippage/MEV/Price Impact.
- Slippage = animated red slime.
- MEV = animated purple hooded rogue with blades.
- Price Impact = animated red spiked beast.
- MEV Bot = large animated robot with pulsing reactor.
- Enemy labels remain above each monster.
- Adds `v15.3 • MONSTERS ON` marker so the deployed build can be verified visually.
