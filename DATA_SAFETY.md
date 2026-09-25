# Watt Street: store privacy answers

These answers are based on what the code does as of 2026-09-25. Checked:

- `Packages/manifest.json`: authentication, cloudsave, remote-config and core. There is no UGS Analytics, Ads, IAP or Firebase package.
- `GridCloudSave.cs`: key `city_v1`, anonymous sign-in, optional Unity account linking with no UI.
- `CityQuestRemoteConfig.cs`
- `Gameplay/Ads/*`: an ad abstraction only, with no network SDK. `AdAnalytics` only writes to the local debug log.
- PlayerPrefs: settings, language and ad cooldowns.
- `Haptics.cs`: local only.
- `UnityConnectSettings`: Analytics and Performance Reporting are off. Cloud Diagnostics crash and exception reporting is **on** (device model, OS, app version, stack trace; no personal data).

Legend: **[NOW]** means true for the current build. **[ADMOB]** means add it when Google AdMob is integrated. **[IAP]** means add it if in-app purchases ship. **[UNITY-ENGINE]** means it depends on the Unity engine settings (see the last section).

## Google Play › Data safety

### Overview questions
| Question | Answer |
|---|---|
| Does your app collect or share any of the required user data types? | **Yes** [NOW] |
| Is all of the user data collected by your app encrypted in transit? | **Yes** (Unity Gaming Services and AdMob use HTTPS/TLS) |
| Do you provide a way for users to request that their data is deleted? | **Yes**. URL: `https://<username>.github.io/wattstreet-legal/delete-data/` |
| Account creation | "My app does not allow users to create an account." The game uses anonymous IDs only. If you enable Unity account linking, reconsider this ("users can create an account via a third-party service" → the deletion URL is already provided). |
| Target audience (App content) | 13–15, 16–17, 18+. Not for children, so the Families policy does not apply. |
| Independent security review | No |

### Data types
"Shared" follows Google's definition: transfers to a **service provider** (Unity, which processes data on our behalf) do **not** count as sharing. Data sent to AdMob **does** count as sharing, because Google is an independent controller for ads.

| Data type (Play category) | Collected | Shared | Ephemeral? | Required / optional | Purposes | When |
|---|---|---|---|---|---|---|
| **App activity › Other actions** (game progress/save, synced to Unity Cloud Save) | Yes | No | No | Required | App functionality | [NOW] |
| **Device or other IDs** (Unity anonymous Player ID, Unity installation ID) | Yes | No | No | Required | App functionality, Fraud prevention/security | [NOW] |
| **Device or other IDs** (Android Advertising ID via AdMob) | Yes | **Yes** (Google) | No | Required* | Advertising or marketing, Analytics, Fraud prevention/security & compliance | [ADMOB] |
| **Location › Approximate location** (AdMob derives it from the IP address) | Yes | **Yes** | No | Required* | Advertising or marketing, Analytics, Fraud prevention | [ADMOB] |
| **App activity › App interactions** (ad views and clicks) | Yes | **Yes** | No | Required* | Advertising or marketing, Analytics | [ADMOB] |
| **App info and performance › Diagnostics** (AdMob SDK diagnostics) | Yes | **Yes** | No | Required* | Analytics, Fraud prevention | [ADMOB] |
| **Financial info › Purchase history** (product ID and order ID only; payment details stay with Google Play) | Yes | No | No | Required for buyers | App functionality | [IAP] |
| **App info and performance › Crash logs** (Unity Cloud Diagnostics) | Yes | No | No | Required | App functionality (fixing bugs) | [NOW] |
| **App info and performance › Diagnostics** (Unity engine hardware statistics) | Yes | No | No | Required | Analytics | [UNITY-ENGINE], only if `submitAnalytics` stays on |

\*The ads themselves are opt-in (rewarded, user-initiated). Once integrated, however, the SDK runs whenever ads are enabled, so Google's own guidance is to declare AdMob data as *not optional*. Cross-check with Google's page "Google Mobile Ads SDK: Play data disclosure" when integrating, because it lists the exact types for the SDK version you use.

Not collected, so leave these unticked: Personal info (name, email, user IDs linked to identity, address, phone), Financial info (card data), Health, Messages, Photos/Videos, Audio, Files, Calendar, Contacts, Precise location, Web browsing, Installed apps, Search history. Support emails arrive outside the app and are not declared.

## Apple App Store › App Privacy ("nutrition label")

**Tracking** (Apple's definition: linking data with third-party data for ads): **No** [NOW]. With [ADMOB] and personalized ads: **Yes**. The Device ID (IDFA) is used for tracking only after ATT consent. In that case add `NSUserTrackingUsageDescription` and show the ATT prompt.

| Apple category | Data type | Purposes | Linked to user? | Used for tracking? | When |
|---|---|---|---|---|---|
| User Content | **Gameplay Content** (cloud save) | App Functionality | Yes (linked to the anonymous User ID) | No | [NOW] |
| Identifiers | **User ID** (Unity Player ID) | App Functionality | Yes | No | [NOW] |
| Identifiers | **Device ID** (IDFA) | Third-Party Advertising, Analytics | Yes | **Yes** (with ATT consent) | [ADMOB] |
| Usage Data | **Advertising Data**, **Product Interaction** | Third-Party Advertising, Analytics | Yes | Yes | [ADMOB] |
| Location | **Coarse Location** (IP-derived) | Third-Party Advertising, Analytics | No | Yes | [ADMOB] |
| Diagnostics | **Crash Data** (Unity Cloud Diagnostics) | App Functionality | No | No | [NOW] |
| Diagnostics | **Other Diagnostic Data / Performance Data** | Analytics | No | No | [ADMOB], and [UNITY-ENGINE] if hardware stats stay on |
| Purchases | **Purchase History** | App Functionality | Yes | No | [IAP] |

Current build without ads: "Data Linked to You" contains Gameplay Content and User ID (both App Functionality). There is no "Data Used to Track You". Age rating: 12+ (the equivalent of a 13+ audience). This is not a "Made for Kids" app.

## Unity engine settings (decide before release)
- `ProjectSettings.asset › submitAnalytics: 1` is the Unity hardware statistics setting.
- `UnityConnectSettings › InsightsSettings.m_EngineDiagnosticsEnabled: 1` is Unity engine diagnostics.

Turn both off if possible (Player Settings / Services), and the [UNITY-ENGINE] rows disappear. If they stay on, follow Unity's current guidance for Google Play Data safety and Apple privacy labels for the Unity runtime, and tick the Diagnostics rows above.

## Keep in sync
If any of these ship, update this file **and** `_src/lang_*.py` (then run `build.py`):

- a new SDK (analytics, crash reporting, IAP, another ad network)
- a new data flow (for example leaderboards or a display name)
