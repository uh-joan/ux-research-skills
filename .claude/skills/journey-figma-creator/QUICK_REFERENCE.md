# Journey Figma Creator - Quick Reference

**Last Updated:** 2026-03-31

## 🚀 Quick Start (Template-Based Approach)

### 1. Preparation (2 minutes)

```bash
# Have these ready:
✅ Persona journey markdown file path
✅ Template SVG or Figma URL (for visual reference)
✅ Figma Desktop Bridge connected
✅ Target Figma file and page name
```

### 2. Create Complete JavaScript File (5-10 minutes)

**File Structure:**
```javascript
// 1. DATA SECTION - Embed all content
const personaData = {
  persona: { name, title, organization, context, team, goal },
  keyInsights: { challenging: [], effortful: [], positive: [] },
  criticalChallenges: [{ title, quote }, ...],
  opportunities: [{ number, title, bullets: [] }, ...],
  phases: [
    { number, title, actions: [], painPoints: [], tools: [] },
    ...
  ]
};

// 2. MAIN FUNCTION - Create everything
async function createJourneyMap() {
  // FIRST: Load ALL fonts
  await figma.loadFontAsync({ family: "Inter", style: "Regular" });
  await figma.loadFontAsync({ family: "Inter", style: "Medium" });
  await figma.loadFontAsync({ family: "Inter", style: "Semi Bold" });
  await figma.loadFontAsync({ family: "Inter", style: "Bold" });

  // Create Section (prevents floating nodes warning)
  const section = figma.createSection();
  section.name = "Journey: " + personaData.persona.name;

  // Create main container
  const mainFrame = figma.createFrame();
  mainFrame.name = personaData.persona.name + " - Journey Map";
  mainFrame.resizeWithoutConstraints(2040, 1190);
  section.appendChild(mainFrame);
  figma.currentPage.appendChild(section);

  // Create panels with ALL visual assets
  const panel1 = createPanel1_Profile(mainFrame);
  const panel2 = createPanel2_Phases1to4(mainFrame);
  const panel3 = createPanel3_Phases5to6(mainFrame);

  // Select and zoom
  figma.currentPage.selection = [mainFrame];
  figma.viewport.scrollAndZoomIntoView([mainFrame]);

  return mainFrame;
}

// 3. HELPER FUNCTIONS - Create visual elements
function createPanel1_Profile(parent) { /* ... */ }
function createPanel2_Phases1to4(parent) { /* ... */ }
function createPanel3_Phases5to6(parent) { /* ... */ }

// 4. EXECUTE
createJourneyMap();
```

### 3. Execute (30 seconds)

```javascript
// Single figma_execute call with entire script
await figma_execute({
  code: readFileSync('persona-journey.js', 'utf8'),
  timeout: 30000
});
```

### 4. Verify (1 minute)

Check console output:
```
✅ Loaded Inter Regular
✅ Loaded Inter Medium
✅ Loaded Inter Semi Bold
✅ Loaded Inter Bold
✅ Journey map created successfully!
📍 Frame ID: 32:1676
```

---

## 📋 Visual Assets Checklist

Copy this checklist for each new journey map:

### Emoji Icons (10 required)
- [ ] 👤 Avatar person icon
- [ ] 😟 Challenging moments emoji
- [ ] 😐 Effortful moments emoji
- [ ] 😊 Positive moments emoji
- [ ] 🏢 Organization icon
- [ ] 💼 Organizational context icon
- [ ] 👥 Team collaboration icon
- [ ] 🎯 Primary goal icon
- [ ] ⚠️ Pain point warning
- [ ] 🔧 Tool indicator

### Geometric Shapes
- [ ] Avatar circle (48px, dark gray #2A2B2D)
- [ ] Phase badges (32px circles, dark gray #2D2D2D, white numbers)
- [ ] Opportunity circles (32px, teal #29BAA0, white numbers)
- [ ] Challenge borders (4px rectangles, red #E74C3C, left edge)

### Color Palette
- [ ] Main background: #F8F8F8
- [ ] Panel backgrounds: #FFFFFF
- [ ] Dark circles: #2A2B2D / #2D2D2D
- [ ] Actions header: #2175C3 (blue)
- [ ] Pain points header: #E74C3C (red)
- [ ] Tools header: Purple-blue (RGB: 0.4, 0.35, 0.7)
- [ ] Opportunity circles: #29BAA0 (teal)
- [ ] Challenge borders: #E74C3C (red)
- [ ] Insight boxes: Light red/yellow/green

### Typography (Inter font family)
- [ ] Regular weight loaded
- [ ] Medium weight loaded
- [ ] Semi Bold weight loaded
- [ ] Bold weight loaded

---

## ⚡ Common Mistakes to Avoid

### ❌ Don't Do This
```javascript
// Splitting across multiple calls
await figma_execute({ code: "const frame = figma.createFrame();" });
await figma_execute({ code: "frame.appendChild(...);" }); // frame is STALE!

// Creating text before loading fonts
const text = figma.createText(); // Will fail!
await figma.loadFontAsync({ family: "Inter", style: "Bold" }); // Too late

// Forgetting visual assets
// Missing emojis, circles, borders → incomplete output

// Wrong RGB values
fills: [{ type: 'SOLID', color: { r: 255, g: 0, b: 0 } }]; // Should be 0-1, not 0-255

// Creating on canvas directly
figma.currentPage.appendChild(frame); // Creates floating nodes warning
```

### ✅ Do This Instead
```javascript
// Everything in ONE execution
await figma_execute({ code: `
  async function complete() {
    // Load fonts FIRST
    await figma.loadFontAsync(...);

    // Create Section → Frame
    const section = figma.createSection();
    const frame = figma.createFrame();
    section.appendChild(frame);
    figma.currentPage.appendChild(section);

    // Add ALL visual assets
    // ... complete implementation
  }
  complete();
` });

// Correct RGB values (0-1)
fills: [{ type: 'SOLID', color: { r: 1, g: 0, b: 0 } }];
```

---

## 🎨 Layout Specifications

### 3-Panel Horizontal Layout (Proven Dimensions)

```
Total: 2040px (W) × 1190px (H)

┌─────────┬─────────┬─────────┐
│ Panel 1 │ Panel 2 │ Panel 3 │
│ Profile │ Phs 1-4 │ Phs 5-6 │
│ 640px   │ 640px   │ 640px   │
│         │         │         │
│ X=20    │ X=680   │ X=1340  │
└─────────┴─────────┴─────────┘
      20px gaps between panels
```

**Panel Contents:**
- **Panel 1 (640px):** Profile + Key Insights + Critical Challenges + Opportunities
- **Panel 2 (640px):** Phases 1-4 vertically stacked
- **Panel 3 (640px):** Phases 5-6 vertically stacked

**Scaling for More Phases:**
- 7-9 phases: Add Panel 4 at X=2000
- 10-12 phases: Add Panel 5 at X=2660
- Keep panel width consistent (640px)

---

## 🔧 Screenshot Strategy

### Choose Based on Width

| Journey Width | Scale | Tool | Notes |
|--------------|-------|------|-------|
| < 2000px | 2 | `figma_take_screenshot` | High quality |
| 2000-4000px | 1 | `figma_take_screenshot` | Good quality |
| 4000-8000px | 1 | `figma_capture_screenshot` | Local rendering |
| > 8000px | - | Skip | Too wide for API |

### Example Usage
```javascript
// For 2040px wide layout (Sample Participant example)
await figma_capture_screenshot({
  format: 'PNG',
  scale: 1, // Not 2! Would exceed API limit
  nodeId: frameId
});
```

**Pro Tip:** If screenshot fails with dimension error, just skip it. The journey map was created successfully - screenshot is optional validation.

---

## 📚 Reference Implementations

### Proven Examples

| File | Layout | Phases | Notes |
|------|--------|--------|-------|
| `DI&A/journey/marcus-chen-template-journey.js` | 3-panel horizontal | 6 | ⭐ GOLD STANDARD - Use as template |
| `.claude/skills/journey-figma-creator/implementation.js` | Multi-panel | Variable | Original implementation |
| `CDDI/journey/persona-journey-*.md` | Individual user | 4-7 | Earlier examples |

### Copy-Paste Patterns

**Pattern 1: Emoji Icon with Circle Background**
```javascript
const circle = figma.createEllipse();
circle.resize(32, 32);
circle.fills = [{ type: 'SOLID', color: { r: 0.17, g: 0.17, b: 0.18 } }];
panel.appendChild(circle);

const emoji = figma.createText();
emoji.characters = "👤";
emoji.fontSize = 16;
emoji.x = circle.x + 8;
emoji.y = circle.y + 6;
panel.appendChild(emoji);
```

**Pattern 2: Bordered Quote Box**
```javascript
const box = figma.createFrame();
box.resizeWithoutConstraints(580, 80);
box.fills = [{ type: 'SOLID', color: { r: 0.99, g: 0.95, b: 0.95 } }];

const border = figma.createRectangle();
border.resize(4, 80); // 4px thick
border.fills = [{ type: 'SOLID', color: { r: 0.91, g: 0.30, b: 0.24 } }]; // Red
box.appendChild(border);

const text = figma.createText();
text.characters = "Quote text here";
text.x = 15;
text.y = 12;
box.appendChild(text);
```

**Pattern 3: Numbered Circle**
```javascript
const circle = figma.createEllipse();
circle.resize(32, 32);
circle.fills = [{ type: 'SOLID', color: { r: 0.16, g: 0.73, b: 0.61 } }]; // Teal

const number = figma.createText();
number.fontName = { family: "Inter", style: "Bold" };
number.fontSize = 16;
number.characters = "1";
number.fills = [{ type: 'SOLID', color: { r: 1, g: 1, b: 1 } }]; // White
number.x = circle.x + 11;
number.y = circle.y + 6;
```

---

## 🐛 Quick Troubleshooting

### Issue: No console output
**Fix:** Check for syntax errors in JavaScript file

### Issue: Fonts fail to load
**Fix:** Wrap in try/catch, continue with fallbacks
```javascript
try {
  await figma.loadFontAsync({ family: "Inter", style: "Bold" });
} catch (e) {
  console.warn("Font load failed, using fallback");
}
```

### Issue: "FLOATING_NODES" warning
**Fix:** Create Section first, then append frame to it
```javascript
const section = figma.createSection();
section.appendChild(mainFrame);
figma.currentPage.appendChild(section);
```

### Issue: Screenshot dimension error
**Fix:** Use scale=1 or skip screenshot
```javascript
// Instead of scale=2, use scale=1
await figma_capture_screenshot({ scale: 1 });
```

### Issue: Missing visual elements
**Fix:** Check emoji unicode characters and RGB values
```javascript
// Verify emoji renders
const test = figma.createText();
test.characters = "👤"; // Should show person icon

// Verify RGB is 0-1, not 0-255
color: { r: 0.91, g: 0.30, b: 0.24 } // Correct
color: { r: 232, g: 77, b: 61 }      // Wrong!
```

---

## 📖 Full Documentation

For complete details, see:
- **LESSONS_LEARNED.md** - Detailed lessons from Sample Participant creation
- **SKILL.md** - Complete skill documentation
- **TEMPLATE_GUIDE.md** - Template creation guide
- **EXECUTION_INSTRUCTIONS.md** - Step-by-step execution guide

---

## ⏱️ Time Estimates

| Task | Time |
|------|------|
| Prepare markdown data | 2-5 min |
| Create JavaScript file | 5-10 min |
| Execute in Figma | 30 sec |
| Verify output | 1 min |
| **Total** | **~10-15 min** |

**Pro Tip:** After first journey map, subsequent ones take 5-7 minutes (copy-paste data structure, update content).

---

**Quick Reference Version 1.0**
**Source:** Sample Participant journey map session (2026-03-31)
