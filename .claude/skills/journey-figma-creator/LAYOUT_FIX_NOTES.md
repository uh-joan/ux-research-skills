# Layout Fix Notes - Journey Map Creation

## Problem Encountered (2026-03-27)

When creating journey maps programmatically, phase frames were created with **fixed width of 100px** while their content (columns container) was **752px wide**. This caused severe content truncation:

- Phase titles cut off ("Receiv" instead of "Receive Global Guidance")
- Only Actions column visible
- Mindsets and Pain Points columns hidden

## Root Cause

Frames were created with:
- `counterAxisSizingMode: 'FIXED'`
- Fixed width not matching content width

## Solution

Set all container frames to **auto-size to their content**:

```javascript
// For phase frames
phase.primaryAxisSizingMode = 'AUTO';  // Hug contents vertically
phase.counterAxisSizingMode = 'AUTO';  // Hug contents horizontally

// For header frames
header.primaryAxisSizingMode = 'AUTO';
header.counterAxisSizingMode = 'AUTO';

// For columns container
columns.primaryAxisSizingMode = 'AUTO';
columns.counterAxisSizingMode = 'AUTO';

// For text nodes
titleText.textAutoResize = 'WIDTH_AND_HEIGHT';  // Allow text to expand
```

## Results

- Phase width changed from 100px → 752px
- All 3 columns now visible (Actions: 282px, Mindsets: 243px, Pain Points: 195px)
- Phase titles display fully
- Content properly contained

## Implementation Guidance

**When creating frames programmatically:**

1. ✅ **DO:** Use `AUTO` sizing for containers that should hug their content
2. ✅ **DO:** Set `textAutoResize = 'WIDTH_AND_HEIGHT'` for dynamic text
3. ❌ **DON'T:** Use fixed widths unless you know the exact content size
4. ❌ **DON'T:** Assume default frame sizing will work - explicitly set it

**Code Pattern:**

```javascript
// Create frame with proper auto-layout
const container = figma.createFrame();
container.layoutMode = 'VERTICAL';  // or 'HORIZONTAL'
container.primaryAxisSizingMode = 'AUTO';  // Hug in primary direction
container.counterAxisSizingMode = 'AUTO';  // Hug in counter direction
container.itemSpacing = 24;
container.paddingLeft = 32;
container.paddingRight = 32;
container.paddingTop = 32;
container.paddingBottom = 32;

// For text that should expand
const text = figma.createText();
await figma.loadFontAsync(text.fontName);
text.textAutoResize = 'WIDTH_AND_HEIGHT';
text.characters = 'Long text that needs to expand...';
```

## Fixed in Code

Applied fix to all 6 phases across 3 pages in Shirley Han's journey map:
- Page 2: Phases 1-4 (100px → 752px)
- Page 3: Phases 5-6 (100px → 752px)

---

**Last Updated:** 2026-03-27
**Context:** Template-based journey map creation using A4 layout
