# Template Structure Analysis

**Template URL:** https://www.figma.com/design/mE4eNMq71OOXSkH4SihpnX/User-journey---template

**Analysis Date:** 2026-03-27

---

## Discovered Structure

```
User journey - template (Frame 1:1382)
├── User journey - Page 1 (Frame 1:1131)
│   Size: 794px × 1190px (A4 portrait at ~96 DPI)
│   Layout: VERTICAL auto-layout
│   Padding: 32px all sides
│   Item Spacing: 24px
│   Background: White (#FFFFFF)
│   Effects: Drop shadow
│   Currently: EMPTY (no children)
│
├── User journey - Page 2 (Frame 1:947)
│   Size: 794px × 1190px (A4 portrait)
│   Layout: VERTICAL auto-layout
│   Padding: 32px all sides
│   Item Spacing: 24px
│   Background: White (#FFFFFF)
│   Effects: Drop shadow
│   Currently: EMPTY (no children)
│   Interaction: Click → Navigate to Page 3
│
└── User journey - Page 3 (Frame 1:1059)
    Size: 794px × 1190px (A4 portrait)
    Layout: VERTICAL auto-layout
    Padding: 32px all sides
    Item Spacing: 24px
    Background: White (#FFFFFF)
    Effects: Drop shadow
    Currently: EMPTY (no children)
```

---

## Key Findings

### 1. Template Type: **Content-Filled Journey Template**

The template is **FULLY POPULATED** with a complete 7-phase journey map example:

**Page 1 (User journey - Page 1):**
- Header section: "disease navigation"
- Complex structured content with frames and containers
- Page number "1" at bottom

**Page 2 (User journey - Page 2):**
- Header: "User journey" title
- 4 Journey Phases:
  - Phase 1: "Define Scope & Gather Initial Inputs" (COMPONENT)
  - Phase 2: "Collect & Triangulate Data Sources"
  - Phase 3: "Build treatment Schemes" (INSTANCE of Phase 1 component)
  - Phase 4: "Build Financial Model"
- Each phase has:
  - Numbered circle badge (1, 2, 3, 4)
  - Phase title text
  - 3-column container (Actions, Mindsets, Tools/Pain Points)
  - Consistent spacing and styling
- Page number "2" at bottom

**Page 3 (User journey - page 3):**
- 3 Journey Phases:
  - Phase 5: "Stakeholder Review"
  - Phase 6: "Finalize Deliverables"
  - Phase 7: "Monitor & Update" (INSTANCE of Phase 1 component)
- Same phase structure as Page 2
- Page number "3" at bottom

**Key Design Elements:**
- ✅ Reusable component: "Frame 9" (Phase 1) is a COMPONENT
- ✅ Component instances: Phases 3, 5, 7 are INSTANCES
- ✅ 3-column layout per phase (282px, 243px, 195px)
- ✅ Numbered badges for phases
- ✅ Consistent vertical auto-layout
- ✅ PDF export configured

### 2. Implications for Implementation

**Current Template Philosophy:**
This is a **CONTENT REPLACEMENT template** - it contains actual journey content that needs to be replaced with user's markdown data.

**Implementation Approach: Clone + Replace**

1. **Clone Template to Current File**
   - Import the entire template frame structure
   - Preserve all styling, components, and layout properties

2. **Identify Phase Frames**
   - Scan for phase structures (numbered frames with titles)
   - Detect pattern: Container with number badge + title + 3-column layout

3. **Replace Content**
   - Update numbered badges (1→N based on markdown phase count)
   - Replace phase title text with markdown phase names
   - Populate 3 columns with:
     - Column 1 (282px): Actions
     - Column 2 (243px): Mindsets/Emotions
     - Column 3 (195px): Pain Points/Tools

4. **Handle Variable Phase Counts**
   - Template has 7 phases (4 on Page 2, 3 on Page 3)
   - If markdown has 5 phases: Use Page 2 + adjust Page 3
   - If markdown has 10 phases: Clone additional phase frames
   - Reuse the component "Frame 9" for consistency

---

## Recommendation: Content Replacement Approach

**For This Specific Template:**

### **Clone + Replace Strategy**

```
1. Clone entire template to current Figma file
2. Find all phase frames (by pattern matching)
3. Replace text content:
   - Phase numbers (in circular badges)
   - Phase titles
   - Column content (actions, mindsets, pain points)
4. Adjust phase count:
   - Delete extra phases if markdown has fewer
   - Clone phase component if markdown has more
5. Update header section on Page 1
```

### **Why This Works:**

- ✅ Preserves exact template design (fonts, colors, spacing, shadows)
- ✅ Maintains component relationships (instances stay linked)
- ✅ Keeps 3-column layout structure
- ✅ Handles variable phase counts elegantly
- ✅ User can update template design independently

---

## Auto-Fill Mode Implementation Plan

### Step 1: Detect Template Type
```javascript
function analyzeTemplate(templateData) {
  const pages = templateData.children.filter(n =>
    n.name.match(/User journey - [Pp]age \d+/i)
  );

  const hasZones = pages.some(page =>
    hasChildrenWithZoneMarkers(page)
  );

  return {
    type: hasZones ? 'zone-based' : 'auto-fill',
    pages: pages,
    pageCount: pages.length
  };
}
```

### Step 2: Clone Template Structure
```javascript
async function cloneTemplate(templateUrl, targetFile) {
  // Fetch template structure
  const templateData = await figma_get_file_data({
    fileUrl: templateUrl,
    depth: 3,
    verbosity: 'full'
  });

  // Find main template frame
  const templateFrame = findFrameByName(templateData, 'User journey - template');

  // Clone to current file using figma_execute
  return await cloneFrameToCurrentFile(templateFrame);
}
```

### Step 3: Fill Pages with Journey Content
```javascript
async function fillTemplatePages(clonedTemplate, journeyData) {
  const pages = clonedTemplate.children;
  const totalPhases = journeyData.phases.length;
  const phasesPerPage = Math.ceil(totalPhases / pages.length);

  for (let i = 0; i < pages.length; i++) {
    const page = pages[i];
    const startIdx = i * phasesPerPage;
    const endIdx = Math.min(startIdx + phasesPerPage, totalPhases);
    const phasesForPage = journeyData.phases.slice(startIdx, endIdx);

    // Generate content into this page
    await fillPageWithPhases(page, phasesForPage, {
      padding: page.paddingLeft, // Use template's padding
      spacing: page.itemSpacing,  // Use template's spacing
      width: page.absoluteBoundingBox.width,
      height: page.absoluteBoundingBox.height
    });
  }
}
```

---

## A4 Layout Specifications

### Page Dimensions
- **Width:** 794px
- **Height:** 1190px
- **Ratio:** ~1:1.5 (A4 portrait)
- **DPI Equivalent:** ~96 DPI (794px ≈ 210mm at 96 DPI)

### Content Area (after padding)
- **Content Width:** 794 - 64 = 730px (32px left + 32px right)
- **Content Height:** 1190 - 64 = 1126px (32px top + 32px bottom)

### Recommended Phase Layout (2 phases per page)
```
Page Layout:
┌────────────────────────────────────┐
│ [32px padding]                     │
│  ┌──────────────┬──────────────┐  │
│  │   Phase 1    │   Phase 2    │  │  Content area: 730px wide
│  │   (341px)    │   (341px)    │  │  Phase width: (730 - 24) / 2 = 353px
│  │              │              │  │  Gap between: 24px
│  └──────────────┴──────────────┘  │
│ [32px padding]                     │
└────────────────────────────────────┘
```

---

## Template Detection Logic

```javascript
function detectTemplateMode(templateFrame) {
  // Check if any child frames have zone markers
  const hasZoneMarkers = (node) => {
    if (node.name.match(/\[([A-Z_]+)(?:_(\d+))?\]/)) {
      return true;
    }
    if (node.children) {
      return node.children.some(hasZoneMarkers);
    }
    return false;
  };

  if (hasZoneMarkers(templateFrame)) {
    return {
      mode: 'zone-based',
      message: 'Template contains zone markers - using zone injection'
    };
  }

  // Check for auto-layout pages
  const pages = templateFrame.children.filter(n =>
    n.type === 'FRAME' && n.layoutMode === 'VERTICAL'
  );

  if (pages.length > 0 && pages.every(p => !p.children || p.children.length === 0)) {
    return {
      mode: 'auto-fill',
      message: 'Template has empty auto-layout pages - using auto-fill mode',
      pages: pages.length
    };
  }

  return {
    mode: 'unsupported',
    message: 'Template structure not recognized'
  };
}
```

---

## Next Steps

1. ✅ Template structure analyzed
2. ⏭ Implement auto-fill mode for blank templates
3. ⏭ Implement zone-based mode for advanced templates
4. ⏭ Add template mode detection
5. ⏭ Update SKILL.md with template modes
6. ⏭ Create TEMPLATE_GUIDE.md for users

---

## Template Creation Guidelines (Future)

### For Auto-Fill Templates:
```
1. Create frames named "User journey - Page N"
2. Set layoutMode: VERTICAL
3. Add padding and itemSpacing
4. Leave frames empty
5. Skill will auto-fill with journey content
```

### For Zone-Based Templates:
```
1. Create frames named "User journey - Page N"
2. Add child frames with zone markers:
   - [HEADER] for title/subtitle
   - [PHASE_COLUMNS_1] for phase content (page 1)
   - [PAIN_POINTS_1] for pain points (page 1)
3. Skill will inject content into zones
```

---

## Conclusion

The current template is a **blank structural template** optimized for auto-fill mode.

**Implementation Priority:**
1. **Phase 1:** Auto-fill mode (works with current template immediately)
2. **Phase 2:** Zone-based mode (for future advanced templates)
3. **Phase 3:** Template validation and error handling
