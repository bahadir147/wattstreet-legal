# Watt Street legal site

This is a static site for **Watt Street: Idle Power Tycoon** (Synverse, `com.synverse.wattstreet`). It holds three documents:

- the privacy policy
- the terms of use
- the data deletion page

Each document is available in 7 languages: en (default), tr, es, pt-BR, de, fr, it. The site has no scripts, cookies or trackers. It follows the device's light/dark setting and is mobile friendly. All internal links are relative, so the site works under the `/wattstreet-legal/` subpath.

## Layout

| Path | Content |
|---|---|
| `index.html`, `<lang>.html` | Landing page (game name + links) |
| `privacy/index.html`, `privacy/<lang>.html` | Privacy Policy |
| `terms/index.html`, `terms/<lang>.html` | Terms of Use |
| `delete-data/index.html`, `delete-data/<lang>.html` | Data deletion instructions |
| `_src/build.py` | Generator. Holds the constants: contact email, links, languages |
| `_src/lang_<code>.py` | Texts per language |
| `DATA_SAFETY.md` | Answers for the Google Play Data safety form and the App Store privacy label |

In every folder, `index.html` is the English version.

## Editing

Change the text in `_src/lang_*.py`. Change the email, the date or the links only in `_src/build.py` (`CONTACT_EMAIL` is the only place the email is set). Then rebuild:

```sh
python3 legal-site/_src/build.py   # rewrites all 28 HTML pages
```

The effective date is written out per language in each `lang_*.py` (`"date"`). Update it in all seven files when a policy changes.

## Publish on GitHub Pages (repo `wattstreet-legal`)

The folder lives inside the game repo. Push only this folder to its own public repo:

```sh
# 1) On GitHub create an empty public repo: <username>/wattstreet-legal (no README).
# 2) From the game repo root:
git subtree push --prefix legal-site https://github.com/<username>/wattstreet-legal.git main
# 3) GitHub › wattstreet-legal › Settings › Pages › Source: "Deploy from a branch",
#    Branch: main, Folder: / (root) › Save. The site is live after about 1 minute.
```

Repeat step 2 after each change. Jekyll skips `_src/`, `README.md` and `DATA_SAFETY.md` (see `_config.yml`).

An alternative is a Synverse organization site. Create the org `synverse` and a repo named `synverse.github.io`, then put this folder under `wattstreet/`. The URLs then become `https://synverse.github.io/wattstreet/privacy/`.

## URLs for the stores

Base: `https://<username>.github.io/wattstreet-legal/`

| Where | Field | URL |
|---|---|---|
| Play Console › App content › Privacy policy | Privacy policy URL | `https://<username>.github.io/wattstreet-legal/privacy/` |
| Play Console › App content › Data safety › Data deletion | "Delete account URL" / data deletion URL | `https://<username>.github.io/wattstreet-legal/delete-data/` |
| Play Console › Store listing (optional) | Website | `https://<username>.github.io/wattstreet-legal/` |
| App Store Connect › App Privacy | Privacy Policy URL | `https://<username>.github.io/wattstreet-legal/privacy/` |
| App Store Connect › App Information (optional) | License Agreement: keep Apple's standard EULA; our terms refer to it | `https://<username>.github.io/wattstreet-legal/terms/` |
| In the game (Settings) | Privacy / Terms links | same URLs, with a per-language page if you like, e.g. `privacy/tr.html` |

## TODO before release

1. **Player ID is not shown in the game.** `GridCloudSave` knows `AuthenticationService.Instance.PlayerId`, but the Settings › "Account & cloud" sheet (`UI/GridHud.Cloud.cs`) never displays it. The deletion page tells players to copy it from there. Add the ID as a copyable/selectable line and a "Privacy policy" link on that sheet.
2. **AdMob is not integrated yet.** The policy already covers it with "if/when available" wording. When you add it:
   - include UMP consent and the in-game "Privacy options" button (the policy mentions it);
   - include `AD_ID`, and ATT with `NSUserTrackingUsageDescription` on iOS;
   - update `DATA_SAFETY.md`;
   - remove the "if/when" wording if you want to.
3. **Unity engine data.** `ProjectSettings/ProjectSettings.asset` has `submitAnalytics: 1` (hardware statistics). `UnityConnectSettings` has `m_EngineDiagnosticsEnabled: 1`. Unity Analytics, Cloud Diagnostics and Performance Reporting are all off (0). The policy mentions only "limited technical information to Unity". Either turn these two off, or declare them as described in `DATA_SAFETY.md`.
4. **Unity account linking.** The code (`GridCloudSave.LinkAccount`, `playerAccountsConfigured: 1`) exists but no UI calls it. The policy covers it as "if available".
5. **In-game deletion (optional).** Unity Authentication supports `DeleteAccountAsync()`. An in-app "Delete cloud data" button would remove the need for email requests. Apple requires in-app deletion only for apps where users create accounts.
6. **Legal review.** The terms name Turkish law as the governing law. Have a lawyer glance at the text if possible. Trademark checks for "Watt Street" are still open.
