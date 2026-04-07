# Journey Map Template Creation Guide

A comprehensive guide for creating Figma templates compatible with the journey-figma-creator skill.

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Template Structure](#template-structure)
3. [Phase Frame Anatomy](#phase-frame-anatomy)
4. [Content Replacement Rules](#content-replacement-rules)
5. [Example Templates](#example-templates)
6. [Testing Your Template](#testing-your-template)
7. [Troubleshooting](#troubleshooting)

---

## Quick Start

### Minimum Viable Template

Create a Figma file with:

1. **Main Container Frame**
   - Name: "User journey - template"
   - Can contain multiple pages

2. **Page Frames** (at least 1)
   - Name pattern: "User journey - Page N" (where N = 1, 2, 3...)
   - Layout: VERTICAL auto-layout recommended
   - Size: Your choice (A4 = 794px × 1190px, Letter = 816px × 1056px, Custom)

3. **Phase Frames** (at least 1 example)
   - Numbered badge: Single-digit text node (1-9)
   - Phase title: Text node with phase name
   - 3-column container: Frames for Actions, Mindsets, Pain Points

### Example Structure

```
User journey - template
├── User journey - Page 1
│   └── (Header content - optional)
├── User journey - Page 2
│   ├── Phase Frame 1
│   │   ├── Number Badge: "1"
│   │   ├── Title: "Phase Name"
│   │   └── 3-Column Container
│   │       ├── Actions Column (282px)
│   │       ├── Mindsets Column (243px)
│   │       └── Pain Points Column (195px)
│   ├── Phase Frame 2
│   └── Phase Frame 3
└── User journey - Page 3
    ├── Phase Frame 4
    └── Phase Frame 5
```

---

## Template Structure

### 1. Main Template Frame

**Required:**
- Frame type: FRAME
- Name: "User journey - template" (exact match) or "Journey Template"
- Contains all page frames as children

**Optional:**
- Can be any size (skill will clone it)
- Can have background styling
- Can include export settings (PDF, PNG, etc.)

### 2. Page Frames

**Required:**
- Frame type: FRAME
- Name pattern: "User journey - Page" + number (e.g., "User journey - Page 1")
- Parent: Main template frame

**Recommended:**
- Layout mode: VERTICAL (for auto-stacking phases)
- Padding: 32-40px (creates white space)
- Item spacing: 24-32px (gap between phases)
- Background: White or light color

**Common Sizes:**
- A4 Portrait: 794px × 1190px (96 DPI)
- A4 Landscape: 1123px × 794px
- Letter Portrait: 816px × 1056px
- US Legal: 816px × 1344px
- Custom Poster: Any size

### 3. Phase Frames

**Critical Components:**

#### a) Numbered Badge
- **Type:** TEXT node
- **Characters:** Single digit "1", "2", "3"... "9"
- **Detection:** Skill finds text nodes with pattern `/^[0-9]$/`
- **Replacement:** Updated to match markdown phase order

**Example:**
```
Frame: "Container"
└── Frame: "Badge Container" (32px × 32px circle)
    └── Text: "1" ← Skill updates this to "5" for Phase 5
```

#### b) Phase Title
- **Type:** TEXT node
- **Characters:** Phase name (5+ characters)
- **Detection:** Skill finds text nodes with length > 5 chars
- **Replacement:** Updated from markdown `### Phase N: [Title]`

**Example:**
```
Text: "Define Scope & Gather Initial Inputs"
↓ (replaced with)
Text: "Receive Global Guidance" ← From markdown
```

#### c) 3-Column Container
- **Type:** FRAME with 3 child frames
- **Layout:** HORIZONTAL (columns side-by-side)
- **Column Widths:**
  - Column 1 (Actions): ~282px
  - Column 2 (Mindsets): ~243px
  - Column 3 (Pain Points): ~195px

**Detection Logic:**
```javascript
// Skill looks for frames with 3 children matching these widths
if (frame.children.length === 3) {
  const widths = [282, 243, 195];
  // Allow ±20px tolerance
  if (widthsMatch(frame.children, widths, tolerance=20)) {
    // This is a 3-column container!
  }
}
```

---

## Phase Frame Anatomy

### Complete Phase Frame Example

```
Phase Frame (730px wide)
├── Frame: "Header" (HORIZONTAL)
│   ├── Frame: "Badge Container" (32px × 32px)
│   │   └── Text: "1" ← NUMBER BADGE (must be single digit)
│   └── Text: "Phase Title" ← TITLE (will be replaced)
│
└── Frame: "Content Container" (HORIZONTAL, 3 columns)
    ├── Frame: "Actions Column" (282px width)
    │   ├── Text: "Label: Actions" (optional header)
    │   ├── Text: "• Action item 1" ← Populated from markdown
    │   ├── Text: "• Action item 2"
    │   └── Text: "• Action item 3"
    │
    ├── Frame: "Mindsets Column" (243px width)
    │   ├── Text: "Label: Mindsets" (optional header)
    │   ├── Text: ""Quote 1"" ← Populated from markdown
    │   └── Text: ""Quote 2""
    │
    └── Frame: "Pain Points Column" (195px width)
        ├── Text: "Label: Pain Points" (optional header)
        ├── Text: "⚠ Pain point 1" ← Populated from markdown
        └── Text: "⚠ Pain point 2"
```

### Styling Freedom

You have complete control over:
- ✅ Colors (backgrounds, borders, text)
- ✅ Typography (fonts, sizes, weights)
- ✅ Spacing (padding, gaps)
- ✅ Effects (shadows, blurs)
- ✅ Corner radius
- ✅ Stroke weights
- ✅ Icons and decorations

**The skill only replaces TEXT content, not styling.**

---

## Content Replacement Rules

### What Gets Replaced

| Element | Detection Pattern | Replacement Source | Format |
|---------|------------------|-------------------|--------|
| **Number Badge** | Single-digit text `/^[0-9]$/` | Phase index (1-N) | Plain number |
| **Phase Title** | Text node >5 chars | `### Phase N: [Title]` | Phase name only |
| **Actions Column** | Column 1 (~282px) | `**Actions:**` section | `• Action text` |
| **Mindsets Column** | Column 2 (~243px) | `**Mindsets:**` section | `"Quote text"` |
| **Pain Points Column** | Column 3 (~195px) | `**Pain Points:**` section | `⚠ Pain text` |

### What's Preserved

- ✅ All styling (colors, fonts, effects)
- ✅ Layout properties (auto-layout, constraints)
- ✅ Component relationships (instances stay linked)
- ✅ Layer names (except text content)
- ✅ Export settings
- ✅ Interactions and prototyping links

### Content Formatting

**Actions Column:**
```markdown
Markdown Input:
**Actions:**
- Review global guidance
- Analyze assumptions

↓

Figma Output:
• Review global guidance
• Analyze assumptions
```

**Mindsets Column:**
```markdown
Markdown Input:
**Mindsets:**
> "How do these apply to Canada?"
- What data can I use?

↓

Figma Output:
"How do these apply to Canada?"
"What data can I use?"
```

**Pain Points Column:**
```markdown
Markdown Input:
**Pain Points:**
- Global guidance focuses on major markets
- Limited Canada-specific data

↓

Figma Output:
⚠ Global guidance focuses on major markets
⚠ Limited Canada-specific data
```

---

## Example Templates

### 1. A4 Multi-Page Template (Your Template)

**File:** https://www.figma.com/design/mE4eNMq71OOXSkH4SihpnX/User-journey---template

**Characteristics:**
- 3 A4 pages (794px × 1190px)
- 7 phases total (4 on Page 2, 3 on Page 3)
- Professional print layout
- Vertical auto-layout
- 32px padding, 24px spacing
- Drop shadows and rounded corners

**Best For:**
- Print deliverables
- Executive presentations
- Client reports
- PDF exports

### 2. Single-Page Horizontal Template (Concept)

**Characteristics:**
- 1 wide page (6000px × 1800px)
- All phases in horizontal flow
- Horizontal auto-layout
- Scrollable canvas view

**Best For:**
- Web display
- Workshop whiteboards
- FigJam migration
- Digital collaboration

### 3. Slide Deck Template (Concept)

**Characteristics:**
- 6-8 pages (1920px × 1080px, 16:9)
- 1 phase per page
- Progressive reveal storytelling
- Prototyping links for navigation

**Best For:**
- Stakeholder presentations
- Step-by-step walkthroughs
- Educational content
- Present mode

---

## Testing Your Template

### Step 1: Validate Structure

**Checklist:**
- [ ] Main frame named "User journey - template"
- [ ] At least 1 page named "User journey - Page N"
- [ ] At least 1 phase frame with numbered badge
- [ ] Phase frame has 3-column container
- [ ] Column widths approximately 282px, 243px, 195px

### Step 2: Test with Sample Markdown

Use this test markdown:

```markdown
# User Journey Map: Template Test

## Actor Profile
**Name:** Test User
**Role:** Tester
**Organization:** Testing Org

## Scenario
**Goal:** Validate template
**Context:** Template testing

## Journey Map

### Phase 1: First Phase
**Timeline:** Now

**Actions:**
- Test action 1
- Test action 2

**Mindsets:**
> "This is a test quote"

**Emotions:** Testing (3/5)

**Pain Points:**
- Test pain point 1
```

### Step 3: Run the Skill

```
Create a journey map from test-journey.md using template https://figma.com/design/YOUR_FILE_KEY/Template
```

### Step 4: Verify Output

Check that:
- [ ] Number badge shows "1"
- [ ] Phase title shows "First Phase"
- [ ] Actions column shows "• Test action 1", "• Test action 2"
- [ ] Mindsets column shows `"This is a test quote"`
- [ ] Pain Points column shows "⚠ Test pain point 1"
- [ ] All styling is preserved

### Step 5: Test Variable Phase Counts

Test with:
- 2 phases (skill should delete extras)
- 5 phases (skill should match template)
- 10 phases (skill should clone additional phases)

---

## Advanced Features

### 1. Using Components

**Benefit:** Consistency + Easy Updates

**Setup:**
1. Create Phase Frame as a COMPONENT (⌘+⌥+K)
2. Name it "Phase Component" or "Frame 9"
3. Use instances for each phase
4. Skill will automatically clone component for additional phases

**Example:**
```
User journey - Page 2
├── Phase Component (COMPONENT) ← Master
├── Phase Instance 1 (INSTANCE) ← Clone of master
├── Phase Instance 2 (INSTANCE) ← Clone of master
└── Phase Instance 3 (INSTANCE) ← Clone of master
```

### 2. Page Numbering

Add page numbers as text nodes:

```
User journey - Page 1
├── (Content)
└── Text: "1" (bottom right, 12px, light gray)
```

Skill will preserve these but won't update them.

### 3. Header/Footer Sections

Add static content that won't be replaced:

```
User journey - Page 1
├── Header Frame
│   ├── Logo
│   ├── Title: "User Journey"
│   └── Date
├── (Phase frames)
└── Footer Frame
    ├── Copyright
    └── Contact Info
```

Skill only modifies phase frames, leaving header/footer intact.

---

## Troubleshooting

### Issue: "Template not found"

**Cause:** Main template frame name doesn't match

**Solution:**
- Ensure frame is named exactly "User journey - template"
- Check for extra spaces or capitalization
- Frame must be top-level in the page (not nested)

### Issue: "No phase frames detected"

**Cause:** Phase frames don't match detection pattern

**Solutions:**
1. Add numbered badge (single-digit text)
2. Add phase title (text >5 characters)
3. Ensure 3-column container has frames ~282, 243, 195px wide

### Issue: "Content not replacing"

**Cause:** Text nodes are locked, grouped, or inside components

**Solutions:**
1. Check text nodes aren't locked (🔒 icon)
2. Ungroup merged text layers
3. For components: expose text as component properties

### Issue: "Layout breaks after generation"

**Cause:** Auto-layout constraints conflict

**Solutions:**
1. Use VERTICAL auto-layout on pages
2. Set phase frames to "Hug contents" or fixed height
3. Remove conflicting constraints

### Issue: "Too many/few phases"

**Cause:** Template has different phase count than markdown

**Expected Behavior:**
- Markdown has fewer phases → Extra template phases deleted
- Markdown has more phases → Phase component cloned to create more

**Verification:**
- Check skill logs for "Adjusted phase count" message
- Verify markdown has correct number of phases

---

## Best Practices

### Design

✅ **DO:**
- Use consistent spacing throughout
- Create reusable phase component
- Test with 3, 5, 7, 10 phases
- Use auto-layout for flexibility
- Include visual examples in template

❌ **DON'T:**
- Merge text layers (skill can't update)
- Use absolute positioning (breaks on resize)
- Mix different phase structures
- Create overly deep nesting (>5 levels)

### File Organization

✅ **DO:**
- Keep template in dedicated file
- Use clear naming ("Company Journey Template v1")
- Document template in file description
- Create template variations (A4, Letter, Poster)
- Version templates (v1, v2, v3)

❌ **DON'T:**
- Mix template with actual journey maps
- Create generic names ("Frame 1", "Group 2")
- Delete pages thinking they're unused

### Performance

✅ **DO:**
- Limit phases per page to 4-5
- Use instances instead of duplicating
- Flatten complex graphics
- Minimize effects (shadows, blurs)

❌ **DON'T:**
- Create 20 phases on one page
- Use heavy background images
- Add unnecessary groups/frames

---

## Template Checklist

Before publishing your template:

**Structure:**
- [ ] Main frame: "User journey - template"
- [ ] Pages: "User journey - Page N"
- [ ] Phase frames with numbered badges
- [ ] 3-column containers (~282, 243, 195px)

**Content:**
- [ ] Example phase titles
- [ ] Sample actions, mindsets, pain points
- [ ] Page numbers (optional)
- [ ] Header/footer (optional)

**Styling:**
- [ ] Colors match brand guidelines
- [ ] Typography is consistent
- [ ] Spacing follows design system
- [ ] Effects are subtle

**Testing:**
- [ ] Test with 2 phases
- [ ] Test with 5 phases
- [ ] Test with 10 phases
- [ ] Verify text replacement works
- [ ] Check PDF export

**Documentation:**
- [ ] File description explains template
- [ ] Template URL is shareable
- [ ] Instructions for users provided

---

## Next Steps

1. **Create Your Template:** Use this guide to build a custom template
2. **Test It:** Run the skill with sample markdown
3. **Refine:** Adjust styling, spacing, and layout
4. **Share:** Provide template URL to your team
5. **Iterate:** Update template based on feedback

**Need Help?**
- Review example template: https://www.figma.com/design/mE4eNMq71OOXSkH4SihpnX/User-journey---template
- Check TEMPLATE_ANALYSIS.md for technical details
- See implementation-template.js for detection logic

---

**Version:** 1.0.0
**Last Updated:** 2026-03-27
**Skill:** journey-figma-creator
