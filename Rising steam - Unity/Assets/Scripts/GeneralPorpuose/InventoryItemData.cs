using System.Collections;
using System.Collections.Generic;
using System.Runtime.CompilerServices;
using UnityEngine;

[CreateAssetMenu (menuName = "Inventory Item Data")]
public class InventoryItemData : ScriptableObject
{
    public Sprite icon;
    public int damageAmount;
    public string damageType;
    public string armourAmmount;
    public GameObject prefab;
    public bool isEquipable;
    public string playerEquiped;
    [TextArea]
    public string description;
    
}
