---
name: journey-figma-creator
description: Create visual user journey maps in Figma from structured markdown journey files. Use when user wants to visualize journey maps in Figma, create presentation-ready journey diagrams, generate design artifacts from research, or transform markdown journey maps into visual timeline layouts with phases, emotions, and touchpoints. Requires Figma Desktop Bridge plugin and existing journey markdown files.
---

# Journey Map Generator

This skill creates visual user journey maps in Figma from structured markdown files following the user journey map format.

## ⚠️ CRITICAL: Always Use Task Tool

**MANDATORY:** Journey maps MUST be created using the Task tool with general-purpose subagent.

**Why:** Figma's plugin API doesn't persist node references across multiple tool calls. If you split creation across multiple `figma_execute` calls, node IDs become stale and the layout breaks.

**Correct Workflow:**
```
Task tool → general-purpose subagent → reads markdown + implementation.js → creates entire journey in ONE execution
```

See "Usage" section below for details.

## Input Format

The skill expects a markdown file with this structure:

```markdown
# User Journey Map: [Title]

## Actor Profile
**Name:** [Name]
**Role:** [Role]
**Organization:** [Organization]
**Team:** [Team description]
**Key Responsibilities:**
- [Responsibility 1]
- [Responsibility 2]

## Scenario
**Goal:** [Main goal]
**Context:** [Context description]
**Expectations:**
- [Expectation 1]
- [Expectation 2]

## Journey Map

### Phase 1: [Phase Name]
**Timeline:** [Timeline description]

**Actions:**
- [Action 1]
- [Action 2]

**Mindsets:**
> "[Quote from user]"

- [Thought/question 1]
- [Thought/question 2]

**Emotions:** [Emotion description] (rating/5)
- [Emotion detail]

**Note:** The first quote in the Mindsets section (text within `> "..."`) will be extracted and displayed as a prominent quote card in Figma for that phase.

**Pain Points:**
- [Pain point 1]
- [Pain point 2]

---

### Phase 2: [Next Phase]
[... same structure ...]

## Emotional Journey
[ASCII chart or description]

## Key Opportunities
### 1. **[Opportunity Name]**
- **Issue:** [Description]
- **Impact:** [Impact description]
- **Success Metric:** [Metrics]
- **Quote:** "[Supporting quote]"
```

## Usage

**CRITICAL: Use Task Tool with General-Purpose Subagent**

When the user provides a markdown file path or asks to create a journey map from a markdown file:

**✅ CORRECT APPROACH (ALWAYS USE THIS):**
```
Use Task tool with:
- subagent_type: "general-purpose"
- description: "Create [journey name] in Figma"
- prompt: "Create complete journey map for [NAME] by:
    1. Reading the journey markdown at [PATH]
    2. Reading .claude/skills/journey-figma-creator/QUICK_REFERENCE.md (critical patterns)
    3. Reading .claude/skills/journey-figma-creator/implementation.js (code structure)
    4. Following DI&A/journey/marcus-chen-template-journey.js as the gold standard implementation
    All steps (font loading, Section creation, frame creation, content) MUST be in ONE figma_execute call."
```

**❌ NEVER DO THIS:**
- Do NOT call `figma_execute` multiple times sequentially
- Do NOT split journey creation across multiple tool calls
- Do NOT try to retrieve nodes with `getNodeByIdAsync` across calls

**Why the Task Tool Approach Works:**
- Creates everything in ONE continuous execution context
- Prevents node ID staleness (nodes become unreachable across multiple `figma_execute` calls)
- Allows the agent to read both the markdown file AND implementation.js reference
- Ensures proper hierarchy (Section > Frame > Children) in single pass
- All fonts loaded at the beginning, all nodes created and parented immediately

**Journey Map Creation Steps (handled by subagent):**

1. Read the markdown file
2. Read the implementation.js reference file
3. Parse the structured content:
   - Actor profile information
   - Scenario details
   - Journey phases with actions, mindsets, emotions, pain points
   - User quotes from Mindsets section (blockquote format: `> "quote"`)
   - Key opportunities
   - Supporting quotes
4. Create complete Figma journey map in ONE execution with:
   - Title and subtitle from Actor Profile
   - Phase headers (colored by phase)
   - Trigger and timeline cards
   - User quote cards (purple-bordered, displayed below trigger in each phase)
   - Action items (green cards)
   - Data sources (blue text)
   - Pain points section (red cards)
   - Tools & systems row (blue cards)
   - Context box (user profile)
   - Key insights box
   - Opportunity areas box

## Design Guidelines

**Layout:**
- Horizontal flow, left to right
- 6000-8000px wide depending on number of phases
- ~1800-2000px height
- Each phase column: ~920-1000px wide

**Color Palette (Helix Design System):**

**IMPORTANT:** Use Helix design tokens whenever possible. Fallback to hardcoded colors only if Helix is unavailable.

| Element | Helix Token | Resolved Value | Fallback (Hardcoded) |
|---------|-------------|----------------|---------------------|
| **Phase Headers** | | | |
| Phase 1 (Initiation) | `surface/info` | #D7E8F7 | #E6F0FF |
| Phase 2 (Data/Research) | `surface/positive` | #D2F7D6 | #D9F2D9 |
| Phase 3 (Building) | `surface/warn` | #FFEFD1 | #FFF2D9 |
| Phase 4 (Validation) | `components/accent/outlined_basic-hover` | #FAF5FF | #F2E6FF |
| Phase 5 (Presentation) | `surface/negative` | #FADCDC | #FFE6E6 |
| Phase 6+ (Additional) | `surface/minimal` | #F2F2F2 | #F2F2D9 |
| **Pain Points** | | | |
| Background | `surface/negative` | #FADCDC | #FFEFEF |
| Border | `components/negative/outline` | #C43136 | #E64D4D |
| Text | `text/negative` | #C43136 | #E64D4D |
| **Tools & Systems** | | | |
| Background | `surface/info` | #D7E8F7 | #F0F5FF |
| Border | `components/accent/outline` | #5E33BF | #B3CCFF |
| **Text Colors** | | | |
| Primary (headers) | `text/primary` | #2A2B2D | #000000 |
| Secondary (labels) | `text/secondary` | #5F6368 | #666666 |
| Disabled (metadata) | `text/disabled` | #BABCBE | #999999 |
| **Spacing** | | | |
| Card padding | `spacing/1` | 8px | 8px |
| Card gaps | `spacing/2` | 16px | 16px |
| Section spacing | `spacing/3` | 24px | 24px |
| Large gaps | `spacing/4` | 32px | 32px |

**Typography:**
- Title: Inter Bold 48px
- Subtitle: Inter Regular 16px
- Phase headers: Inter Semi Bold 20px
- Section labels: Inter Semi Bold 14px
- Action items: Inter Regular 11px
- Pain points: Inter Regular 10px

**Components:**
- Triggers: Yellow/orange background (#FFF9E6)
- Quotes: Light purple background (#FAFAFF) with purple border (#B3B3E6), opening quote mark (")
- Actions: Green cards with light border
- Pain points: Red-bordered cards with warning icon (⚠)
- Data sources: Blue text below actions
- Tools: Light blue cards at bottom

## Execution Steps (Performed by Task Agent in ONE Continuous Execution)

**CRITICAL: All steps must happen in ONE continuous `figma_execute` call. DO NOT split across multiple calls.**

1. **Load ALL fonts at the very beginning (FIRST STEP):**
   ```javascript
   await figma.loadFontAsync({ family: "Inter", style: "Bold" });
   await figma.loadFontAsync({ family: "Inter", style: "Regular" });
   await figma.loadFontAsync({ family: "Inter", style: "Medium" });
   await figma.loadFontAsync({ family: "Inter", style: "Semi Bold" });
   ```
   - **Critical:** Must load fonts BEFORE creating any text nodes
   - Failure to do this causes silent errors or crashes

2. **Create Section → Frame hierarchy immediately:**
   ```javascript
   const section = figma.createSection();
   section.name = "[Journey Name]";
   const mainFrame = figma.createFrame();
   mainFrame.name = "Journey Map";
   section.appendChild(mainFrame);
   figma.currentPage.appendChild(section);
   ```
   - **Never create nodes on blank canvas**
   - Always use Section as container
   - Always `appendChild()` immediately after creation

3. **Parse the markdown:**
   - Extract actor profile (name, role, org, responsibilities)
   - Extract scenario (goal, context, expectations)
   - Identify all phases (marked by `### Phase N:`)
   - For each phase extract: timeline, actions, mindsets (including first blockquote as main quote), emotions, pain points
   - Extract key opportunities section

4. **Calculate layout:**
   - Count number of phases
   - Calculate total width: `40 + (numPhases * 960) + 40`
   - Determine starting X position for each phase: `40 + (index * 960)`

5. **Create complete Figma structure in same context:**
   - Create and populate title and subtitle
   - Create phase header frames (colored by phase - cycle through blue, green, orange, purple, pink, yellow)
   - For each phase, create and populate ALL elements:
     - Trigger card (yellow) with timeline and emotion rating
     - Quote card (light purple with border) if quote exists
     - "Actions:" label
     - Action items as green cards
     - Data sources text if applicable
   - Create pain points row (red, spanning all phases)
   - Create tools row (blue, spanning all phases)
   - Create context boxes at bottom

6. **Add pain points row:**
   - Create pain points header (red, full width)
   - For each phase, create pain point cards vertically
   - Use warning icon (⚠) prefix
   - Background: `{r: 1, g: 0.94, b: 0.94}` (light red)
   - Border: `{r: 0.77, g: 0.19, b: 0.21}` (red)

7. **Add tools row:**
   - Create tools header (blue, full width)
   - Extract tools from actions/context
   - Create tool cards for each phase
   - Background: `{r: 0.94, g: 0.97, b: 1}` (light blue)

8. **Add context boxes:**
   - Context & User Profile (left): Actor profile + scenario
   - Key Insights (middle): Extracted from emotional journey analysis
   - Opportunity Areas (right): Top opportunities from the list

9. **Screenshot validation (OPTIONAL - choose scale by journey width):**

   | Journey Width | Scale | Tool |
   |---|---|---|
   | <2000px | 2 | `figma_take_screenshot` |
   | 2000-4000px | 1 | `figma_take_screenshot` |
   | 4000-8000px | 1 | `figma_capture_screenshot` |
   | >8000px | — | Skip (too wide for API) |

   - DO NOT screenshot journeys >8000px wide — API will return 400 error
   - For >6 phases or wide layouts: skip screenshot, the map was created successfully

---

## 🎨 Template Mode (NEW)

**Use external Figma templates for journey map generation.**

### When to Use Template Mode

Use template mode when you have:
- ✅ A pre-designed journey map template in Figma
- ✅ Specific brand guidelines requiring custom layouts
- ✅ A4/Letter page formats for printing
- ✅ Existing design system components to reuse

### Template Mode Command

```
Create a journey map from /path/to/user-journey.md using template https://figma.com/design/abc123/Template
```

Or use the template URL shorthand:

```
Create journey map from user-journey.md in https://figma.com/design/abc123/Template
```

### How Template Mode Works

1. **Clone Template:** Imports template structure to current file
2. **Find Phases:** Detects phase frames by pattern (numbered badges + titles)
3. **Replace Content:** Updates phase numbers, titles, and column content
4. **Adjust Count:** Adds/removes phases to match markdown data
5. **Preserve Design:** Keeps all styling, components, and layout properties

### Template Requirements

Your Figma template should have:

**Required Structure:**
- Frame named "User journey - template" (or similar)
- Page frames named "User journey - Page N"
- Phase frames with:
  - Numbered badge (circular text with digit 1-9)
  - Phase title (text node)
  - 3-column container layout

**Example Template:**
https://www.figma.com/design/mE4eNMq71OOXSkH4SihpnX/User-journey---template

**Content Replacement:**
- Column 1 (Actions): Populated from `**Actions:**` section
- Column 2 (Mindsets): Populated from `**Mindsets:**` section
- Column 3 (Pain Points): Populated from `**Pain Points:**` section

### Template Mode: Node ID Staleness Warning

**CRITICAL:** Template Mode is also subject to the node ID staleness constraint.

- ✅ Clone template AND populate all content in ONE `figma_execute` call
- ❌ DO NOT clone template in one call, then look up nodes by ID in a second call
- ❌ DO NOT use `getNodeByIdAsync()` across separate `figma_execute` calls

If template cloning and content population must be split, fall back to Default Mode (implementation.js).

### Template Mode Best Practices

✅ **DO:**
- Use templates with consistent phase structure
- Include reusable components for phases (for clean cloning)
- Test template with variable phase counts (3-10 phases)
- Keep template in separate file (easier to update)

❌ **DON'T:**
- Use templates with hardcoded/merged text layers
- Create overly complex nested structures
- Mix different phase layouts on same template

### Template vs Default Mode

| Feature | Default Mode | Template Mode |
|---------|-------------|---------------|
| **Layout** | Horizontal scroll, 960px columns | Custom (A4, poster, etc.) |
| **Styling** | Helix tokens + fallback colors | Your template design |
| **Flexibility** | Fixed layout logic | Adapts to template |
| **Setup** | Zero setup | Requires template creation |
| **Best For** | Quick generation, web display | Print, brand consistency |

### Fallback Behavior

If template mode fails (template not found, invalid structure, etc.):
- ✅ Skill automatically falls back to default mode
- ✅ Generates journey using `implementation.js` logic
- ✅ User receives warning message about fallback

---

## Example Commands

**Default Mode (No Template):**
```
Create a journey map from /path/to/user-journey.md
```

**Template Mode:**
```
Create a journey map from DI&A/user-journey-shirley.md using template https://www.figma.com/design/mE4eNMq71OOXSkH4SihpnX/User-journey---template
```

**Batch Creation with Template:**
```
Create journey maps using template https://figma.com/design/abc123/A4-Template from:
- DI&A/user-journey-shirley.md
- DI&A/user-journey-alex.md
- DI&A/user-journey-maria.md
```

## Best Practices (Lessons Learned)

**📚 For detailed lessons from real-world implementations, see [LESSONS_LEARNED.md](./LESSONS_LEARNED.md)**

### ✅ DO:

1. **Use Task tool with general-purpose subagent for ALL journey map creation**
   - Keeps everything in one execution context
   - Avoids node ID staleness
   - Subagent can read both markdown file AND implementation.js reference

2. **Load ALL fonts at the very beginning**
   - Before creating any text nodes
   - Include all needed styles (Bold, Regular, Semi Bold, etc.)
   - Use try/catch for graceful fallback

3. **Create hierarchy immediately: Section → Frame → Children**
   - Don't create orphaned nodes
   - Always `appendChild()` right after creation
   - Prevents "FLOATING_NODES" housekeeping warnings

4. **Include ALL visual assets explicitly**
   - Emoji icons (👤 😟 😐 😊 🏢 💼 👥 🎯 ⚠️ 🔧)
   - Geometric shapes (circles for badges, rectangles for borders)
   - Exact color values (RGB 0-1 format)
   - See LESSONS_LEARNED.md for complete checklist

5. **Follow proven reference implementations**
   - Sample Participant example: `DI&A/journey/sample-participant-template-journey.js`
   - CDDI examples: Individual user journey maps
   - Reference: `.claude/skills/journey-figma-creator/implementation.js`

6. **Create all content in one continuous script**
   - Don't split across multiple `figma_execute` calls
   - If complex, use Task agent (ALWAYS recommended)
   - Embed all data in the script (persona, phases, insights, opportunities)

7. **Include explicit instructions in Task prompt:**
   - "DO NOT clear or delete any existing content in the Figma file on other pages"
   - "Only work on the new page [PAGE_NAME]"
   - "Create everything in ONE continuous execution"

8. **Use appropriate screenshot scale for large layouts**
   - Journey < 4000px wide: scale=2 ✅
   - Journey 4000-8000px wide: scale=1 ✅
   - Journey > 8000px wide: skip screenshot or use figma_capture_screenshot ✅

### ❌ DON'T:

1. **Don't split Figma creation across multiple sequential tool calls**
   - Node references become stale
   - Layout breaks
   - Hard to debug

2. **Don't create text nodes before loading fonts**
   - Will fail silently or throw errors
   - Always load fonts FIRST

3. **Don't use `getNodeByIdAsync` to retrieve nodes across tool calls**
   - Unreliable in plugin context
   - Better to create everything in one pass

4. **Don't create nodes on blank canvas**
   - Always create Section first
   - Place everything inside
   - Prevents housekeeping warnings

5. **Don't use scale=2 for wide layouts (>4000px)**
   - Will exceed 8000px API dimension limit
   - Use scale=1 or figma_capture_screenshot instead
   - Or skip screenshot entirely for very wide journeys

6. **Don't skip visual assets**
   - Missing emojis, circles, or borders makes output look incomplete
   - Always reference template visually, not just structurally
   - View SVG templates as images to see ALL assets

## Error Handling

Common errors and their solutions:

### Markdown Issues
- If markdown structure is incomplete, ask user which sections are missing
- If no phases found, suggest the markdown format expected

### Figma Connection
- If Figma file not connected, prompt user to provide Figma URL
- If Desktop Bridge not responding, ask user to restart plugin

### Screenshot Dimension Errors
- **Error:** `API Error: 400 - image dimensions exceed max allowed size: 8000 pixels`
- **Cause:** Journey map dimensions × scale > 8000px
- **Solutions:**
  1. Use scale=1 instead of scale=2: `figma_take_screenshot({ scale: 1 })`
  2. Use local screenshot: `figma_capture_screenshot({ scale: 1 })`
  3. Skip screenshot for very wide journeys (>6000px wide)
  4. Screenshot individual panels instead of full layout

### Font Loading Failures
- Use try/catch blocks around font loading
- Log warnings but continue execution with fallback fonts
- Common issue: Font name case-sensitivity

### Floating Nodes Warning
- **Warning:** `FLOATING_NODES: N nodes placed directly on the page canvas`
- **Cause:** Created frames directly on canvas instead of inside Section
- **Fix:** Always create Section → Frame hierarchy (see LESSONS_LEARNED.md)

### Task Agent Failures
- Check that implementation.js path is correct and accessible
- Verify markdown file path exists
- Ensure sufficient permissions on Figma file

### Visual Assets Missing
- Reference LESSONS_LEARNED.md for complete visual assets checklist
- View template as image (not just structure) to identify all required elements
- Verify emoji unicode characters are correct

## Helix Design System Integration

**Helix File:** `https://www.figma.com/design/pI4MbkwcVXdqrqFRi7YhLt/Helix--LS-H-`

### Token Fetching Code Example

```javascript
// Fetch Helix tokens at the start of journey map generation
const helixTokens = {};

try {
  // Fetch Tokens collection (surface, text, components, border)
  const tokensData = await figma_get_variables({
    fileUrl: 'https://www.figma.com/design/pI4MbkwcVXdqrqFRi7YhLt/Helix--LS-H-',
    format: 'filtered',
    collection: 'Tokens',
    verbosity: 'standard',
    resolveAliases: true
  });

  // Fetch Primitives collection (spacing)
  const primitivesData = await figma_get_variables({
    fileUrl: 'https://www.figma.com/design/pI4MbkwcVXdqrqFRi7YhLt/Helix--LS-H-',
    format: 'filtered',
    collection: 'Primitives',
    verbosity: 'standard',
    resolveAliases: true
  });

  // Build lookup map
  [...tokensData.data.variables, ...primitivesData.data.variables].forEach(v => {
    helixTokens[v.name] = {
      id: v.id,
      type: v.resolvedType,
      value: v.resolvedValuesByMode['Mode 1'].value
    };
  });

  console.log('✅ Helix tokens loaded:', Object.keys(helixTokens).length, 'tokens');
} catch (error) {
  console.warn('⚠️ Helix tokens unavailable, using fallback colors');
}
```

### Applying Tokens in figma_execute

```javascript
// Helper: Convert hex to RGB
function hexToRgb(hex) {
  const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
  return result ? {
    r: parseInt(result[1], 16) / 255,
    g: parseInt(result[2], 16) / 255,
    b: parseInt(result[3], 16) / 255
  } : {r: 0, g: 0, b: 0};
}

// Helper: Get color value (Helix or fallback)
function getColor(helixTokenName, fallbackHex) {
  if (helixTokens[helixTokenName]) {
    return hexToRgb(helixTokens[helixTokenName].value);
  }
  return hexToRgb(fallbackHex);
}

// Example: Apply phase header color
const phaseTokens = [
  'surface/info',      // Phase 1
  'surface/positive',  // Phase 2
  'surface/warn',      // Phase 3
  'components/accent/outlined_basic-hover', // Phase 4
  'surface/negative'   // Phase 5
];
const fallbackColors = ['#E6F0FF', '#D9F2D9', '#FFF2D9', '#F2E6FF', '#FFE6E6'];

phaseHeaderFrame.fills = [{
  type: 'SOLID',
  color: getColor(phaseTokens[phaseIndex], fallbackColors[phaseIndex])
}];

// Example: Apply pain point colors
painPointCard.fills = [{
  type: 'SOLID',
  color: getColor('surface/negative', '#FADCDC')
}];
painPointCard.strokes = [{
  type: 'SOLID',
  color: getColor('components/negative/outline', '#C43136')
}];

// Example: Apply text color
headerText.fills = [{
  type: 'SOLID',
  color: getColor('text/primary', '#2A2B2D')
}];

// Example: Use spacing tokens
const cardPadding = helixTokens['spacing/2']?.value || 16;
const sectionGap = helixTokens['spacing/3']?.value || 24;
```

### Key Token Mappings

**Phase Headers:**
- Phase 1: `surface/info` → #D7E8F7
- Phase 2: `surface/positive` → #D2F7D6
- Phase 3: `surface/warn` → #FFEFD1
- Phase 4: `components/accent/outlined_basic-hover` → #FAF5FF
- Phase 5: `surface/negative` → #FADCDC

**Pain Points:**
- Background: `surface/negative` → #FADCDC
- Border: `components/negative/outline` → #C43136

**Tools:**
- Background: `surface/info` → #D7E8F7
- Border: `components/accent/outline` → #5E33BF

**Text:**
- Headers: `text/primary` → #2A2B2D
- Labels: `text/secondary` → #5F6368

**Spacing:**
- Card padding: `spacing/1` → 8px
- Card gaps: `spacing/2` → 16px
- Section spacing: `spacing/3` → 24px

## Tools to Use

- `Read` - to read the markdown file
- `mcp__figma-console__figma_get_variables` - to fetch Helix design tokens
- `mcp__figma-console__figma_navigate` - if Figma URL needed
- `mcp__figma-console__figma_execute` - to create all Figma elements
- `mcp__figma-console__figma_capture_screenshot` - to validate with scale=1

## Notes

- **Helix tokens FIRST:** Always attempt to fetch Helix design tokens at the beginning of journey map generation
- **Graceful fallback:** If Helix fetch fails, log warning and use fallback hardcoded colors
- **Brand consistency:** Using Helix ensures journey maps match organizational design system
- Always create inside a Section, never on blank canvas
- Load Inter font family (Regular, Medium, Semi Bold, Bold)
- Use `resizeWithoutConstraints` for frames
- Use `appendChild` to maintain hierarchy
- For large journeys (>6 phases), reduce phase width to fit
- Validate with screenshot before completing
