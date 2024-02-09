using System;
using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
//using UnityEditorInternal.Profiling.Memory.Experimental;
using UnityEngine;
using UnityEngine.UIElements;
//using static UnityEditor.Progress;
using static UnityEngine.Rendering.DebugUI;

public class InventorySystem : MonoBehaviour
{
    public List<InventoryItem> inventory = new List<InventoryItem>();
    //private Dictionary<InventoryItemData, InventoryItem> itemDictionary = new Dictionary<InventoryItemData, InventoryItem>();
    private bool PlayerHasItem;


    private InventoryItem ItemStored(int index)
    {
        return inventory[index];
    }
    public int InventoryItemCount()
    {
        return inventory.Count;
    }
    public InventoryItemData ItemZeroInInventory()
    {
        return null;
    }
    public void AddItem(InventoryItem Item ,int RecivedStackSize)
    {
        PlayerHasItem = false;

        InventoryItemData NewItemName = Item.ItemData;

        foreach (InventoryItem PlayerItem in inventory)
        {
            if (PlayerItem.ItemData == NewItemName)
            {
                PlayerHasItem = true;
                Debug.Log(PlayerHasItem);
            }
        }
        if (!PlayerHasItem)
        {
            inventory.Add(Item);
        }
        foreach (InventoryItem PlayerItem in inventory)
        {
            if (PlayerItem.ItemData == NewItemName)
            {
                PlayerItem.AddToStack(RecivedStackSize);
            }
        }
    }
    public void RemoveItem(InventoryItem RemovedItem, int RemovedStackSize)
    {
        InventoryItemData RemovedItemName = RemovedItem.ItemData;

        for (int i = 0; i < inventory.Count; i++)
        {
            if (inventory[i].ItemData == RemovedItemName)
            {
                inventory[i].RemoveFromStack(RemovedStackSize);

                if (inventory[i].StackSize <= 0)
                {
                    inventory.RemoveAt(i);
                }

                break; // Item found and processed, exit the loop
            }
        }

        //foreach(InventoryItem Item in inventory)
        //{
        //    if (Item.ItemData == RemovedItemName)
        //    {
        //        Item.RemoveFromStack(RemovedStackSize);
        //    }
        //}

        //for (int i = 0; i < InventoryItemCount(); i++)
        //{
        //    InventoryItemData TargetItem = inventory[i].ItemData;
        //    if (RemovedItemName == TargetItem)
        //    {
        //       inventory[i].RemoveFromStack(RemovedStackSize);
        //    }
        //    if (inventory[i].StackSize == 0)
        //    {
        //        inventory.Remove(inventory[i]);
        //    }
        //}
    }

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    //internal void Remove()
    //{
    //    throw new NotImplementedException();
    //}
}
