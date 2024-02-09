using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.Events;
//using static UnityEditor.Searcher.SearcherWindow.Alignment;

public class PlayerCharacter : MonoBehaviour
{
    [SerializeField] private float speed = 5;
    [SerializeField] private float MoveLimiter = 0.7f;
    [SerializeField] private float ForceAplied = 100000f;
    [SerializeField] private GameManager gameManager;
    private Rigidbody2D RigidBody;
    private Rigidbody2D MovableObjectRB;
    private Animator animator;
    private SpriteRenderer sprite;

    private GameObject ObjectType;
    private InventorySystem ObjectChestInventory;

    private InventorySystem ObjectDoorInventory;
    private BoxCollider2D ObjectDoorCollider;
    
    private InventorySystem PlayerInventory;
    private InventoryItemData DoorKey;
    private InventoryItemData PlayerItem;

    private bool comeBack = true;
    public UnityEvent ChestSound = new UnityEvent();
    public UnityEvent DoorSound = new UnityEvent();



    private void OnTriggerStay2D(Collider2D collision)
    {
        ObjectType = collision.gameObject;
        if (ObjectType.CompareTag("Chest"))
        {
            animator.SetTrigger("isInteracting");
            //Debug.Log("cofre");
            ObjectChestInventory = ObjectType.GetComponent<InventorySystem>();
        }
        if (ObjectType.CompareTag("Door"))
        {
            animator.SetTrigger("isInteracting");
            //Debug.Log("puerta interactuable");
            ObjectDoorInventory = ObjectType.GetComponent<InventorySystem>();
            ObjectDoorCollider = ObjectType.GetComponent<BoxCollider2D>();

            DoorKey = ObjectDoorInventory.inventory[0].ItemData;
            //Debug.Log(DoorKey);
        }
    }

    private void OnCollisionEnter2D(Collision2D collision)
    {
        //if (ObjectType.CompareTag("enemy 1"))
        //{
        //    UnityEngine.Debug.Log("Enemy");
        //    SceneLoader.Load(SceneLoader.Scene.BattleScene1);
        //}
        //if (ObjectType.CompareTag("enemy 2"))
        //{
        //    UnityEngine.Debug.Log("Enemy");
        //    SceneLoader.Load(SceneLoader.Scene.BattleScene1);
        //}
        if (ObjectType.CompareTag("Enemy"))
        {
            GameManager.Instance.UpdateCharacterPos(this.gameObject);
            if(ObjectType.TryGetComponent<EnemyPatrol>(out EnemyPatrol enemy))
            {
                if (enemy.combatInt ==1)
                {
                    GameManager.Instance.combat1 = false;
                }
                if (enemy.combatInt == 2)
                {
                    GameManager.Instance.combat2 = false;
                }
                if (enemy.combatInt == 4)
                {
                    GameManager.Instance.combat4 = false;
                }
                if (enemy.combatInt == 5)
                {
                    GameManager.Instance.combat5 = false;
                }
                SceneLoader.Load(enemy.Escena);
            }
        }
    }
    private void OnCollisionStay2D(Collision2D collision)
    {
        if (ObjectType.CompareTag("MovableObject"))
        {
            MovableObjectRB = collision.gameObject.GetComponent<Rigidbody2D>();
            //Debug.Log(MovableObjectRB);
            Vector2 forceDirection = collision.contacts[0].normal;
            Vector2 force = forceDirection.normalized * -ForceAplied;
            MovableObjectRB.AddForce(force);
        }
    }

    //private void MoveObject()
    //{
    //    if (MoveingObject)
    //    {
    //        float vertical = Input.GetAxis("Vertical");
    //        float horizontal = Input.GetAxis("Horizontal");

    //        Vector2 PushDirection = GetComponent<Rigidbody2D>().velocity.normalized;
    //        MovableObjectRB.AddForce(PushDirection * ForceAplied, ForceMode2D.Impulse);
    //    }
    //}

    private void PlayerInteraction()
    {
        if (ObjectType != null)
        {
            if (Input.GetButtonDown("Interact"))
            {
                if (ObjectType.CompareTag("Chest"))
                {
                    if (ObjectChestInventory.InventoryItemCount() > 0)
                    {
                        ChestSound.Invoke();

                        UnityEngine.Debug.Log(ObjectChestInventory.inventory[0].StackSize);
                        PlayerInventory.AddItem(ObjectChestInventory.inventory[0], ObjectChestInventory.inventory[0].StackSize);
                        UnityEngine.Debug.Log(ObjectChestInventory.inventory[0].StackSize);
                        ObjectChestInventory.RemoveItem(ObjectChestInventory.inventory[0], ObjectChestInventory.inventory[0].StackSize);
                        Destroy(ObjectChestInventory);
                    }
                }
                if (ObjectType.CompareTag("Door"))
                {
                    DoorSound.Invoke();

                    for (int i = 0; i < PlayerInventory.InventoryItemCount() ; i++)
                    {
                        PlayerItem = PlayerInventory.inventory[i].ItemData;
                        if (PlayerItem == DoorKey)
                        {
                            ObjectDoorCollider.gameObject.SetActive(false);
                            PlayerInventory.RemoveItem(PlayerInventory.inventory[i], 1);
                        }
                    }

                }
                if (ObjectType.CompareTag("Enemy"))
                {
                    //Debug.Log("enemy");
                }
            }
        }
        
    }

    // Start is called before the first frame update
    void Start()
    {
        comeBack = true;
        sprite = gameObject.GetComponent<SpriteRenderer>();
        animator = GetComponent<Animator>();
        PlayerInventory = GetComponent<InventorySystem>();
        RigidBody = GetComponent<Rigidbody2D>();
    }

    private void Awake()
    {
        comeBack = true;
    }
    private void FixedUpdate()
    {
        float vertical = Input.GetAxis("Vertical");
        float horizontal = Input.GetAxis("Horizontal");

        if (horizontal != 0 && vertical != 0) // Check for diagonal movement
        {
            // limit movement speed diagonally, so you move at 70% speed
            horizontal *= MoveLimiter;
            vertical *= MoveLimiter;
        }
        if (horizontal != 0 || vertical != 0)
        {
            animator.SetBool("isWalking", true);
            if (horizontal < 0)
            {
                
                sprite.flipX = true;
            }else
            {
                sprite.flipX = false;
            }
        }
        else
        {
            animator.SetBool("isWalking", false);
        }
        RigidBody.velocity = new Vector2(horizontal * speed, vertical * speed);
        //Vector2 MovementDirection = new Vector2(horizontal, vertical);
        //MovementDirection.Normalize();
        //this.RigidBody.AddForce(MovementDirection * speed,ForceMode2D.Impulse);
    }

    // Update is called once per frame
    void Update()
    {
        if (comeBack)
        {
            this.gameObject.transform.position = GameManager.Instance.postCharPos();
            comeBack = false;
        }
        PlayerInteraction();
        //MoveObject();



    }
}