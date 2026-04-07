# Journey Figma Creator - Lessons Learned

**Last Updated:** 2026-03-31
**Source:** Sample Participant journey map creation session (DI&A project)

## Overview

This document captures critical lessons from real-world journey map creation to help future implementations succeed on the first try.

---

## ✅ What Worked: The Winning Approach

### 1. Direct JavaScript Execution with ALL Visual Assets

**Success Pattern:**
```javascript
// Create a COMPLETE 962-line JavaScript file with:
// 1. All data embedded (persona info, phases, challenges, opportunities)
// 2. ALL visual assets (emojis, circles, borders, colors)
// 3. Complete layout logic (3-panel structure)
// 4. Execute via figma_execute in ONE call

const sampleParticipantData = {
  persona: { name, title, org, ... },
  keyInsights: { challenging, effortful, positive },
  criticalChallenges: [...],
  opportunities: [...],
  phases: [...]
};

async function createMarcusChenJourneyMap() {
  // Load ALL fonts first
  await figma.loadFontAsync({ family: "Inter", style: "Regular" });
  // ... load all variants

  // Create main container
  const mainFrame = figma.createFrame();

  // Create 3 panels with all visual elements
  const panel1 = createPanel1_Profile(mainFrame);
  const panel2 = createPanel2_Phases1to4(mainFrame);
  const panel3 = createPanel3_Phases5to6(mainFrame);

  return mainFrame;
}

createMarcusChenJourneyMap();
```

**Why This Works:**
- ✅ Everything in ONE execution context
- ✅ No node ID staleness issues
- ✅ All visual assets explicitly defined
- ✅ Clean, reproducible output

**File Reference:**
`[PROJECT]/journey/participant-template-journey.js` (962 lines, 32KB)

---

## 🎨 Complete Visual Assets Checklist

### Critical Success Factor
**You CANNOT skip any of these visual elements.** Previous attempts failed because they were missing.

### Emoji Icons Required

| Icon | Unicode | Usage | Location |
|------|---------|-------|----------|
| 👤 | U+1F464 | Avatar person | Profile section |
| 😟 | U+1F61F | Challenging moments | Key insights column 1 |
| 😐 | U+1F610 | Effortful moments | Key insights column 2 |
| 😊 | U+1F60A | Positive moments | Key insights column 3 |
| 🏢 | U+1F3E2 | Organization | Profile: organization |
| 💼 | U+1F4BC | Organizational context | Profile: context |
| 👥 | U+1F465 | Team collaboration | Profile: team |
| 🎯 | U+1F3AF | Primary goal | Profile: goal |
| ⚠️ | U+26A0 | Pain point indicator | Phase pain points |
| 🔧 | U+1F527 | Tool indicator | Phase tools |

**Implementation Example:**
```javascript
// Avatar circle with person icon
const avatarCircle = figma.createEllipse();
avatarCircle.resize(48, 48);
avatarCircle.fills = [{ type: 'SOLID', color: { r: 0.17, g: 0.17, b: 0.18 } }];

const avatarIcon = figma.createText();
avatarIcon.characters = "👤"; // Person emoji
avatarIcon.fontSize = 24;
```

### Geometric Visual Elements

#### 1. Avatar Circle
- **Type:** Ellipse
- **Size:** 48px × 48px
- **Fill:** Dark gray #2A2B2D (RGB: 0.17, 0.17, 0.18)
- **Icon:** 👤 (24px, centered)

#### 2. Phase Badges
- **Type:** Ellipse
- **Size:** 32px × 32px
- **Fill:** Dark gray #2D2D2D (RGB: 0.17, 0.17, 0.18)
- **Number:** White text, Inter Bold 16px, centered
- **Usage:** One per phase (1-6)

#### 3. Challenge Borders (RED)
- **Type:** Rectangle
- **Size:** 4px wide × box height
- **Fill:** Red #E74C3C (RGB: 0.91, 0.30, 0.24)
- **Position:** Left edge of challenge box
- **Box Background:** Light pink #FCF3F3 (RGB: 0.99, 0.95, 0.95)

#### 4. Opportunity Circles (TEAL)
- **Type:** Ellipse
- **Size:** 32px × 32px
- **Fill:** Teal #29BAA0 (RGB: 0.16, 0.73, 0.61)
- **Number:** White text, Inter Bold 16px, centered
- **Usage:** One per opportunity (1-4)

### Color Palette (Exact Values)

#### Structural Colors
```javascript
const colors = {
  // Backgrounds
  mainBackground: { r: 0.98, g: 0.98, b: 0.98 }, // #F8F8F8
  panelBackground: { r: 1, g: 1, b: 1 },         // #FFFFFF

  // Avatar & Badges
  darkCircle: { r: 0.17, g: 0.17, b: 0.18 },     // #2A2B2D, #2D2D2D
  whiteText: { r: 1, g: 1, b: 1 },               // #FFFFFF

  // Key Insights Boxes
  challengingBg: { r: 0.98, g: 0.85, b: 0.85 },  // Light red
  effortfulBg: { r: 1, g: 0.95, b: 0.8 },        // Light yellow
  positiveBg: { r: 0.85, g: 0.95, b: 0.85 },     // Light green

  // Critical Challenges
  challengeBorder: { r: 0.91, g: 0.30, b: 0.24 }, // #E74C3C red
  challengeBg: { r: 0.99, g: 0.95, b: 0.95 },     // #FCF3F3 light pink

  // Opportunities
  opportunityCircle: { r: 0.16, g: 0.73, b: 0.61 }, // #29BAA0 teal

  // Column Headers
  actionsHeader: { r: 0.13, g: 0.46, b: 0.76 },   // #2175C3 blue
  painPointsHeader: { r: 0.91, g: 0.30, b: 0.24 }, // #E74C3C red
  toolsHeader: { r: 0.4, g: 0.35, b: 0.7 },        // Purple-blue

  // Text
  primaryText: { r: 0, g: 0, b: 0 },              // Black
  secondaryText: { r: 0.3, g: 0.3, b: 0.3 },      // Dark gray
  labelText: { r: 0.5, g: 0.5, b: 0.5 }           // Medium gray
};
```

### Typography System

```javascript
const typography = {
  // Font loading (CRITICAL: Load ALL variants upfront)
  fonts: [
    { family: "Inter", style: "Regular" },
    { family: "Inter", style: "Medium" },
    { family: "Inter", style: "Semi Bold" },
    { family: "Inter", style: "Bold" }
  ],

  // Font sizes by element
  sizes: {
    personaName: 24,        // "Sample Participant"
    sectionTitle: 16,       // "Critical Challenges"
    phaseTitle: 14,         // "Receive Request & Define Scope"
    profileContent: 13,     // Organization, team, goal text
    sectionLabel: 12,       // "ORGANIZATION", "TEAM COLLABORATION"
    columnHeader: 11,       // "ACTIONS", "PAIN POINTS", "TOOLS"
    contentText: 10,        // Action items, pain points
    insightItems: 9         // Key insights bullets
  }
};
```

---

## 🐛 Common Failures and Fixes

### Failure #1: Missing Visual Assets
**Symptom:** Journey map created but looks "close" - missing emojis, circles, or borders

**Root Cause:** Template only showed text structure, not visual decorations

**Fix:** Use SVG template as visual reference
```bash
# Convert SVG to image for visual inspection
qlmanage -t -s 2000 -o /tmp "User journey - template.svg"
# View the generated thumbnail to see ALL assets
```

**Lesson:** ALWAYS view the template as an image, not just read markdown structure

---

### Failure #2: Screenshot Dimension Error
**Symptom:** `API Error: 400 - image dimensions exceed max allowed size: 8000 pixels`

**Root Cause:** Journey map is 2040px wide, but at scale=2 it becomes 4080px (still under limit). However, if the journey has more phases or larger dimensions, it can exceed 8000px.

**Fix:** Use lower scale for screenshots
```javascript
// ❌ DON'T: Default scale=2 for large layouts
figma_take_screenshot({ format: 'png', scale: 2 })

// ✅ DO: Use scale=1 or 0.5 for wide journey maps
figma_take_screenshot({ format: 'png', scale: 1 })

// ✅ BEST: Use figma_capture_screenshot (local plugin rendering)
figma_capture_screenshot({ format: 'PNG', scale: 1 })
```

**When to Skip Screenshots:**
- Journey maps > 6000px wide
- Multi-page templates (A4 portrait stacked vertically)
- Templates with >8 phases

**Alternative:** Screenshot individual panels instead of full journey

---

### Failure #3: Floating Nodes Warning
**Symptom:** `FLOATING_NODES: 5 nodes placed directly on the page canvas`

**Root Cause:** Created frames directly on canvas instead of inside a Section

**Fix:** Always create Section → Frame hierarchy
```javascript
// ❌ DON'T: Create frame directly on page
const mainFrame = figma.createFrame();
figma.currentPage.appendChild(mainFrame);

// ✅ DO: Create Section first, then frame inside
const section = figma.createSection();
section.name = "Sample Participant Journey";

const mainFrame = figma.createFrame();
mainFrame.name = "Journey Map";
section.appendChild(mainFrame);

figma.currentPage.appendChild(section);
```

---

### Failure #4: Font Loading After Text Creation
**Symptom:** Text nodes fail silently or throw errors

**Root Cause:** Created text nodes before loading fonts

**Fix:** Load ALL fonts at the VERY beginning
```javascript
async function createJourneyMap() {
  // ✅ FIRST: Load all fonts
  const fontsToLoad = [
    { family: "Inter", style: "Regular" },
    { family: "Inter", style: "Medium" },
    { family: "Inter", style: "Semi Bold" },
    { family: "Inter", style: "Bold" }
  ];

  for (const font of fontsToLoad) {
    try {
      await figma.loadFontAsync(font);
      console.log(`✅ Loaded ${font.family} ${font.style}`);
    } catch (e) {
      console.warn(`⚠️ Could not load ${font.family} ${font.style}`);
    }
  }

  // NOW create text nodes
  const text = figma.createText();
  text.fontName = { family: "Inter", style: "Bold" };
  text.characters = "Sample Participant";
}
```

---

### Failure #5: Node ID Staleness Across Calls
**Symptom:** `Error: Cannot find node with ID '123:456'`

**Root Cause:** Tried to split journey creation across multiple `figma_execute` calls

**Fix:** Create everything in ONE execution
```javascript
// ❌ DON'T: Split across multiple calls
figma_execute({ code: "const frame = figma.createFrame(); return frame.id;" })
// Later...
figma_execute({ code: "const frame = figma.getNodeById('123:456'); // FAILS" })

// ✅ DO: Create everything in single execution
figma_execute({ code: `
  async function createComplete() {
    // Load fonts
    // Create all frames
    // Populate all content
    // Return result
  }
  createComplete();
` })
```

---

## 📐 Layout Specifications

### 3-Panel Horizontal Layout

**Proven Dimensions (Sample Participant Example):**
```
Total Canvas: 2040px (W) × 1190px (H)

Panel 1 (Profile):
- Position: X=20, Y=20
- Size: 640px × 1150px
- Background: White (#FFFFFF)
- Corner Radius: 8px
- Content:
  - Profile section (~350px height)
  - Key Insights (3 columns, ~200px height)
  - Critical Challenges (~250px height)
  - Top Opportunities (~350px height)

Panel 2 (Phases 1-4):
- Position: X=680, Y=20
- Size: 640px × 1150px
- Background: White
- Corner Radius: 8px
- Content: Phases 1-4 vertically stacked

Panel 3 (Phases 5-6):
- Position: X=1340, Y=20
- Size: 640px × 1150px
- Background: White
- Corner Radius: 8px
- Content: Phases 5-6 vertically stacked

Gaps:
- Outer margin: 20px
- Panel gap: 20px (680 - 640 - 20)
```

**Scaling Rules:**
- For more phases: Add panels (Panel 4, Panel 5, etc.) at X += 660
- For fewer phases: Reduce panel count
- Panel width should stay consistent (640px) for readability

---

## 🚀 Recommended Workflow

### Step-by-Step Process That Works

1. **Read the persona journey markdown file**
```javascript
const journeyData = await readMarkdownFile('persona-journey-sample-participant.md');
```

2. **Extract visual template reference (if available)**
```bash
# If SVG template exists, generate thumbnail for visual inspection
qlmanage -t -s 2000 -o /tmp "User journey - template.svg"
```

3. **Create complete JavaScript file with embedded data**
```javascript
// Structure:
// 1. Data object (persona, insights, challenges, opportunities, phases)
// 2. Helper functions (createPanel1, createPanel2, addPhaseSection, etc.)
// 3. Main function (createJourneyMap)
// 4. Execution call
```

4. **Execute via figma_execute in ONE call**
```javascript
await figma_execute({
  code: readFileSync('sample-participant-template-journey.js', 'utf8'),
  timeout: 30000 // Allow up to 30 seconds for complex layouts
});
```

5. **Verify success via console output**
```
🚀 Starting Sample Participant journey map creation...
✅ Loaded Inter Regular
✅ Loaded Inter Medium
✅ Loaded Inter Semi Bold
✅ Loaded Inter Bold
✅ Journey map created successfully!
📍 Frame ID: 32:1676
```

6. **Optional: Screenshot for validation (use low scale)**
```javascript
// Only for journeys < 6000px wide
await figma_capture_screenshot({
  format: 'PNG',
  scale: 1, // Not 2!
  nodeId: '32:1676'
});
```

7. **Handle housekeeping warnings**
```javascript
// If you get "FLOATING_NODES" warning:
// 1. Select the created frames
// 2. Group into Section manually, OR
// 3. Update script to create Section first (preferred)
```

---

## 📋 Pre-Flight Checklist

Before creating a journey map, verify:

### Data Preparation
- [ ] Persona journey markdown file exists and is complete
- [ ] File has all required sections (Profile, Insights, Phases, Opportunities)
- [ ] Phase count is known (determines panel count)

### Visual Assets
- [ ] Template visual reference available (SVG, Figma URL, or screenshot)
- [ ] All emoji icons identified (avatar, insights, phase indicators)
- [ ] Color palette extracted (backgrounds, borders, text colors)
- [ ] Typography specifications known (font family, sizes, weights)

### Figma Environment
- [ ] Figma Desktop Bridge plugin connected
- [ ] Target file and page determined
- [ ] Edit permissions confirmed
- [ ] Sufficient canvas space available

### Code Preparation
- [ ] Complete JavaScript file created with ALL visual assets
- [ ] All fonts specified (Inter: Regular, Medium, Semi Bold, Bold)
- [ ] Section → Frame hierarchy included
- [ ] Data embedded or imported correctly

### Execution
- [ ] Code file size reasonable (<100KB)
- [ ] Timeout set appropriately (30s for complex layouts)
- [ ] Screenshot strategy decided (scale=1 or skip for large layouts)

---

## 🔍 Debugging Tips

### If Journey Map Doesn't Appear

**Check Console Output:**
```javascript
// Look for these success messages:
"✅ Loaded Inter [style]"  // All fonts loaded?
"✅ Journey map created successfully!"  // Main function completed?
"📍 Frame ID: [id]"  // Frame was created and has valid ID?
```

**Common Issues:**
1. **No console output** → Script didn't execute (syntax error?)
2. **Font loading fails** → Check font names (case-sensitive)
3. **Frame created but empty** → Check data object population
4. **Frame created off-canvas** → Check X/Y positioning (should be 0 or 20)

### If Visual Assets Are Missing

**Emoji Issues:**
```javascript
// Verify emoji characters are correct
const emojiTest = figma.createText();
emojiTest.characters = "👤"; // Should render person icon
// If blank: system doesn't support emoji
// If shows differently: wrong unicode character
```

**Color Issues:**
```javascript
// Verify RGB values are 0-1, not 0-255
// ❌ Wrong: { r: 255, g: 0, b: 0 }
// ✅ Correct: { r: 1, g: 0, b: 0 }
```

**Circle/Border Issues:**
```javascript
// Verify shapes are created and appended
const circle = figma.createEllipse();
circle.resize(32, 32); // MUST call resize
panel.appendChild(circle); // MUST append to parent
```

### If Layout Breaks

**Check Auto-Resize:**
```javascript
// Text nodes need proper auto-resize
textNode.resize(contentWidth, textNode.height);
textNode.textAutoResize = "HEIGHT"; // Allows vertical growth

// Frames need explicit sizing
frame.resizeWithoutConstraints(640, 1150);
```

**Check Positioning:**
```javascript
// Use absolute positioning, not relative
node.x = 30; // Absolute position within parent
node.y = 100; // Absolute position within parent

// NOT: node.x += 30; (relative - can accumulate errors)
```

---

## 📚 Reference Implementation

**File:** `[PROJECT]/journey/participant-template-journey.js`

**Key Sections to Reference:**
- Lines 1-110: Data structure (sampleParticipantData object)
- Lines 112-140: Main function with font loading
- Lines 142-190: Panel 1 (Profile) creation
- Lines 192-250: Profile section with icons
- Lines 252-290: Key Insights with emoji columns
- Lines 292-330: Critical Challenges with red borders
- Lines 332-370: Top Opportunities with teal circles
- Lines 372-410: Panel 2 (Phases 1-4)
- Lines 412-450: Panel 3 (Phases 5-6)
- Lines 452-520: Phase section helper function

**Reusable Patterns:**
```javascript
// Pattern 1: Emoji icon with background
const circle = figma.createEllipse();
circle.resize(32, 32);
circle.fills = [{ type: 'SOLID', color: darkGray }];
const icon = figma.createText();
icon.characters = "👤";
icon.fontSize = 16;

// Pattern 2: Bordered box
const box = figma.createFrame();
const border = figma.createRectangle();
border.resize(4, box.height);
border.fills = [{ type: 'SOLID', color: red }];
box.appendChild(border);

// Pattern 3: Text with icon prefix
const text = figma.createText();
text.characters = "🔧 Excel";
```

---

## 🎯 Success Criteria

A journey map is correctly implemented when:

### Visual Fidelity
- ✅ All emoji icons render correctly
- ✅ All geometric shapes (circles, borders) present
- ✅ Colors match specification exactly
- ✅ Typography hierarchy is clear
- ✅ Layout is balanced and aligned

### Technical Quality
- ✅ No console errors
- ✅ All fonts loaded successfully
- ✅ Frame hierarchy is clean (Section → Frame → Children)
- ✅ No floating nodes warning
- ✅ Frame is selectable and editable

### Content Accuracy
- ✅ Persona name and title correct
- ✅ All phases present (none missing)
- ✅ Phase numbers sequential (1, 2, 3...)
- ✅ Actions, pain points, tools populated
- ✅ Insights categorized correctly (challenging/effortful/positive)
- ✅ Opportunities numbered and described

### User Experience
- ✅ Journey map fits on canvas
- ✅ Readable at 100% zoom
- ✅ Exportable to PNG/PDF
- ✅ Can be moved/resized without breaking
- ✅ Screenshot works (with scale=1)

---

## 💡 Future Improvements

Based on this session, consider adding:

1. **Visual Asset Library**
   - Create reusable components for common elements (avatar circles, phase badges)
   - Store in shared Figma library

2. **Automated Screenshot Fallback**
   - Detect journey width before screenshotting
   - Auto-adjust scale: <4000px → scale=2, <8000px → scale=1, >8000px → skip

3. **Template Validation**
   - Check template has all required visual elements before cloning
   - Warn user if template is incomplete

4. **Multi-Page Support**
   - For very wide journeys (10+ phases), split into multiple pages
   - Create pagination navigation

5. **Export Presets**
   - A4 PDF export settings
   - Letter PDF export settings
   - PNG at 2x for web

---

## 🏆 Key Takeaways

1. **Complete, Not Iterative**
   - Create the ENTIRE journey in ONE execution
   - Don't split across multiple figma_execute calls

2. **Visual Assets Are NOT Optional**
   - Every emoji, circle, and border matters
   - Reference the SVG template visually, not just structurally

3. **Font Loading Is Critical**
   - Load ALL font variants FIRST
   - Use try/catch to handle missing fonts gracefully

4. **Screenshot Dimensions Matter**
   - Large layouts (>4000px) need scale=1, not scale=2
   - Consider skipping screenshot for very wide journeys

5. **Housekeeping Prevents Warnings**
   - Always create Section → Frame hierarchy
   - Never create nodes directly on canvas

6. **Reference Implementation Exists**
   - sample-participant-template-journey.js is the proven pattern
   - Copy structure, adapt data

---

**End of Lessons Learned**
