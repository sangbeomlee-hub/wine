name	comctl32
type	win32
init	COMCTL32_LibMain

# Functions exported by the Win95 comctl32.dll 
# (these need to have these exact ordinals, because some win95 dlls 
#  import comctl32.dll by ordinal)
#   This list was created from a comctl32.dll v4.72 (IE4.01).

  2 stdcall MenuHelp(long long long long long long ptr) MenuHelp
  3 stdcall ShowHideMenuCtl(long long ptr) ShowHideMenuCtl
  4 stdcall GetEffectiveClientRect(long long long) GetEffectiveClientRect
  5 stdcall DrawStatusTextA(long ptr str long) DrawStatusTextA
  6 stdcall CreateStatusWindowA(long str long long) CreateStatusWindowA
  7 stdcall CreateToolbar(long long long long long long ptr long) CreateToolbar
  8 stdcall CreateMappedBitmap(long long long ptr long) CreateMappedBitmap
  9 stdcall DPA_LoadStream(ptr ptr long long) DPA_LoadStream
 10 stdcall DPA_SaveStream(long long long long) DPA_SaveStream
 11 stdcall DPA_Merge(ptr ptr long ptr ptr long) DPA_Merge
#12 stub Cctl1632_ThunkData32
 13 stdcall MakeDragList(long) MakeDragList
 14 stdcall LBItemFromPt(long long long) LBItemFromPt
 15 stdcall DrawInsert(long long long) DrawInsert
 16 stdcall CreateUpDownControl(long long long long long long long long long long long long) CreateUpDownControl
 17 stdcall InitCommonControls() InitCommonControls
 18 stdcall CreatePropertySheetPage(ptr) CreatePropertySheetPageA
 19 stdcall CreatePropertySheetPageA(ptr) CreatePropertySheetPageA
 20 stdcall CreatePropertySheetPageW(ptr) CreatePropertySheetPageW
 21 stdcall CreateStatusWindow(long str long long) CreateStatusWindowA
 22 stdcall CreateStatusWindowW(long wstr long long) CreateStatusWindowW
 23 stdcall CreateToolbarEx(long long long long long long ptr long long long long long long) CreateToolbarEx
 24 stdcall DestroyPropertySheetPage(long) DestroyPropertySheetPage
 25 stdcall DllGetVersion(ptr) COMCTL32_DllGetVersion
 26 stub DllInstall
 27 stdcall DrawStatusText(long ptr ptr long) DrawStatusTextA
 28 stdcall DrawStatusTextW(long ptr wstr long) DrawStatusTextW
 29 stdcall FlatSB_EnableScrollBar (long long long) FlatSB_EnableScrollBar
 30 stdcall FlatSB_GetScrollInfo (long long ptr) FlatSB_GetScrollInfo
 31 stdcall FlatSB_GetScrollPos (long long) FlatSB_GetScrollPos
 32 stdcall FlatSB_GetScrollProp (long long ptr) FlatSB_GetScrollProp
 33 stdcall FlatSB_GetScrollRange (long long ptr ptr) FlatSB_GetScrollRange
 34 stdcall FlatSB_SetScrollInfo (long long ptr long) FlatSB_SetScrollInfo
 35 stdcall FlatSB_SetScrollPos (long long long long) FlatSB_SetScrollPos
 36 stdcall FlatSB_SetScrollProp (long long long long) FlatSB_SetScrollProp
 37 stdcall FlatSB_SetScrollRange (long long long long long) FlatSB_SetScrollRange
 38 stdcall FlatSB_ShowScrollBar (long long long) FlatSB_ShowScrollBar
 39 stdcall ImageList_Add(ptr long long) ImageList_Add
 40 stdcall ImageList_AddIcon(ptr long) ImageList_AddIcon
 41 stdcall ImageList_AddMasked(ptr long long) ImageList_AddMasked
 42 stdcall ImageList_BeginDrag(ptr long long long) ImageList_BeginDrag
 43 stdcall ImageList_Copy(ptr long ptr long long) ImageList_Copy
 44 stdcall ImageList_Create(long long long long long) ImageList_Create
 45 stdcall ImageList_Destroy(ptr) ImageList_Destroy
 46 stdcall ImageList_DragEnter(long long long) ImageList_DragEnter
 47 stdcall ImageList_DragLeave(long) ImageList_DragLeave
 48 stdcall ImageList_DragMove(long long) ImageList_DragMove
 49 stdcall ImageList_DragShowNolock(long) ImageList_DragShowNolock
 50 stdcall ImageList_Draw(ptr long long long long long) ImageList_Draw
 51 stdcall ImageList_DrawEx(ptr long long long long long long long long long) ImageList_DrawEx
 52 stdcall ImageList_DrawIndirect(ptr) ImageList_DrawIndirect
 53 stdcall ImageList_Duplicate(ptr) ImageList_Duplicate
 54 stdcall ImageList_EndDrag() ImageList_EndDrag 
 55 stdcall ImageList_GetBkColor(ptr) ImageList_GetBkColor
 56 stdcall ImageList_GetDragImage(ptr ptr) ImageList_GetDragImage
 57 stdcall ImageList_GetIcon(ptr long long) ImageList_GetIcon
 58 stdcall ImageList_GetIconSize(ptr ptr ptr) ImageList_GetIconSize
 59 stdcall ImageList_GetImageCount(ptr) ImageList_GetImageCount
 60 stdcall ImageList_GetImageInfo(ptr long ptr) ImageList_GetImageInfo
 61 stdcall ImageList_GetImageRect(ptr long ptr) ImageList_GetImageRect
 62 stdcall ImageList_LoadImage(long str long long long long long) ImageList_LoadImageA
 63 stdcall ImageList_LoadImageA(long str long long long long long) ImageList_LoadImageA
 64 stdcall ImageList_LoadImageW(long wstr long long long long long) ImageList_LoadImageW
 65 stdcall ImageList_Merge(ptr long ptr long long long) ImageList_Merge
 66 stdcall ImageList_Read(ptr) ImageList_Read
 67 stdcall ImageList_Remove(ptr long) ImageList_Remove
 68 stdcall ImageList_Replace(ptr long long long) ImageList_Replace
 69 stdcall ImageList_ReplaceIcon(ptr long long) ImageList_ReplaceIcon
 70 stdcall ImageList_SetBkColor(ptr long) ImageList_SetBkColor
 71 stdcall Alloc(long) COMCTL32_Alloc
 72 stdcall ReAlloc(ptr long) COMCTL32_ReAlloc
 73 stdcall Free(ptr) COMCTL32_Free
 74 stdcall GetSize(ptr) COMCTL32_GetSize
 75 stdcall ImageList_SetDragCursorImage(ptr long long long) ImageList_SetDragCursorImage
 76 stdcall ImageList_SetFilter(ptr long long) ImageList_SetFilter
 77 stdcall ImageList_SetIconSize(ptr long long) ImageList_SetIconSize
 78 stdcall ImageList_SetImageCount(ptr long) ImageList_SetImageCount
 79 stdcall ImageList_SetOverlayImage(ptr long long) ImageList_SetOverlayImage
 80 stdcall ImageList_Write(ptr ptr) ImageList_Write
 81 stdcall InitCommonControlsEx(ptr) InitCommonControlsEx
 82 stdcall InitializeFlatSB(long) InitializeFlatSB
 83 stdcall PropertySheet(ptr) PropertySheetA
 84 stdcall PropertySheetA(ptr) PropertySheetA
 85 stdcall PropertySheetW(ptr) PropertySheetW
 86 stdcall UninitializeFlatSB(long) UninitializeFlatSB
 87 stub _TrackMouseEvent

151 stdcall CreateMRUListA(ptr) CreateMRUListA
152 stdcall FreeMRUList(ptr) FreeMRUListA
153 stub AddMRUStringA@8
154 stub EnumMRUListA@16
155 stub FindMRUStringA@12
156 stub DelMRUString@8
157 stdcall CreateMRUListLazyA(ptr long long long) CreateMRUListLazyA

163 stub CreatePage
164 stub CreateProxyPage

167 stdcall AddMRUData(ptr long long) AddMRUData
169 stdcall FindMRUData(ptr long long long) FindMRUData

233 stdcall Str_GetPtrA(str str long) Str_GetPtrA
234 stdcall Str_SetPtrA(str str) Str_SetPtrA
235 stdcall Str_GetPtrW(wstr wstr long) Str_GetPtrW
236 stdcall Str_SetPtrW(wstr wstr) Str_SetPtrW

320 stdcall DSA_Create(long long) DSA_Create
321 stdcall DSA_Destroy(ptr) DSA_Destroy
322 stdcall DSA_GetItem(ptr long long) DSA_GetItem
323 stdcall DSA_GetItemPtr(ptr long) DSA_GetItemPtr
324 stdcall DSA_InsertItem(ptr long long) DSA_InsertItem
325 stdcall DSA_SetItem (ptr long long) DSA_SetItem
326 stdcall DSA_DeleteItem(ptr long) DSA_DeleteItem
327 stdcall DSA_DeleteAllItems(ptr) DSA_DeleteAllItems
328 stdcall DPA_Create(long) DPA_Create
329 stdcall DPA_Destroy(ptr) DPA_Destroy
330 stdcall DPA_Grow(ptr long) DPA_Grow
331 stdcall DPA_Clone(ptr ptr) DPA_Clone
332 stdcall DPA_GetPtr(ptr long) DPA_GetPtr
333 stdcall DPA_GetPtrIndex(ptr ptr) DPA_GetPtrIndex
334 stdcall DPA_InsertPtr(ptr long ptr) DPA_InsertPtr
335 stdcall DPA_SetPtr(ptr long ptr) DPA_SetPtr
336 stdcall DPA_DeletePtr(ptr long) DPA_DeletePtr
337 stdcall DPA_DeleteAllPtrs(ptr) DPA_DeleteAllPtrs
338 stdcall DPA_Sort(ptr ptr long) DPA_Sort
339 stdcall DPA_Search(ptr ptr long ptr long long) DPA_Search
340 stdcall DPA_CreateEx(long long) DPA_CreateEx
341 stdcall SendNotify(long long long ptr) COMCTL32_SendNotify
342 stdcall SendNotifyEx(long long long ptr long) COMCTL32_SendNotifyEx

350 stdcall StrChrA(str str) COMCTL32_StrChrA
351 stdcall StrRChrA(str str long) COMCTL32_StrRChrA
352 stdcall StrCmpNA(str str long) COMCTL32_StrCmpNA
353 stub StrCmpNIA
354 stdcall StrStrA(str str) COMCTL32_StrStrA
355 stdcall StrStrIA(str str) COMCTL32_StrStrIA
356 stdcall StrCSpnA(str str) COMCTL32_StrCSpnA
357 stdcall StrToIntA(str) COMCTL32_StrToIntA
358 stdcall StrChrW(wstr long) COMCTL32_StrChrW
359 stdcall StrRChrW(wstr wstr long) COMCTL32_StrRChrW
360 stdcall StrCmpNW(wstr wstr long) COMCTL32_StrCmpNW
361 stub StrCmpNIW
362 stdcall StrStrW(wstr wstr) COMCTL32_StrStrW
363 stub StrStrIW
364 stdcall StrSpnW(wstr wstr) COMCTL32_StrSpnW
365 stub StrToIntW
366 stub StrChrIA
367 stub StrChrIW
368 stub StrRChrIA
369 stub StrRChrIW

372 stub StrRStrIA
373 stub StrRStrIW
374 stub StrCSpnIA
375 stub StrCSpnIW
376 stub IntlStrEqWorkerA@16
377 stub IntlStrEqWorkerW@16

382 stub SmoothScrollWindow@4
383 stub DoReaderMode@4
384 stub SetPathWordBreakProc@8
385 stdcall DPA_EnumCallback(long long long) DPA_EnumCallback
386 stdcall DPA_DestroyCallback(ptr ptr long) DPA_DestroyCallback
387 stdcall DSA_EnumCallback(ptr ptr long) DSA_EnumCallback
388 stdcall DSA_DestroyCallback(ptr ptr long) DSA_DestroyCallback
389 stub COMCTL32_389
390 stub COMCTL32_390

400 stub CreateMRUListW@4
401 stub AddMRUStringW@8
402 stub FindMRUStringW@12
403 stub EnumMRUListW@16
404 stub CreateMRUListLazyW@16

410 stub COMCTL32_410
411 stub COMCTL32_411
412 stub COMCTL32_412
413 stub COMCTL32_413

