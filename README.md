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
