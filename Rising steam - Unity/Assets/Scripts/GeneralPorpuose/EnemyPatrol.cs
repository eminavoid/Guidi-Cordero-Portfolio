using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyPatrol : MonoBehaviour
{
    [SerializeField] public Transform PatrolStart;
    [SerializeField] public Transform PatrolEnd;
    [SerializeField] public Transform PatrolCenter;
    [SerializeField] public Transform TargetPlayer;
    [SerializeField] public SceneLoader.Scene Escena;
    
    [SerializeField] public float PatrolSpeed = 2f;
    [SerializeField] public float ChaseSpeed = 8f;
    [SerializeField] public bool horizontal;
    [SerializeField] public bool vertical;
    [SerializeField] public bool diagonalUR;

    [SerializeField] public int combatInt;

    private Animator animator;
    private Rigidbody2D rb;
    private Vector2 MoveDirection;
    private GameObject ObjectInRange;
    private bool PlayerInRange;
    private bool InPatrolRoute;
    private SpriteRenderer sprite;


    
    private void OnTriggerEnter2D(Collider2D collision)
    {
        ObjectInRange = collision.gameObject;
        if (ObjectInRange.CompareTag("Player"))
        {
            PlayerInRange = true;
        }
    }
    private void OnTriggerExit2D(Collider2D collision)
    {
        ObjectInRange = collision.gameObject;
        if (ObjectInRange.CompareTag("Player"))
        {
            PlayerInRange = false;
        }
    }

    private void ChasePlayer()
    {
        InPatrolRoute = false;
        Vector3 direction = (TargetPlayer.position - transform.position).normalized;
        rb.velocity = direction * ChaseSpeed;
    }
    private void Patrol()
    {
        animator.SetBool("isWalking", true);
        if (InPatrolRoute)
        {
             if (horizontal)
             {
                 if (Vector2.Distance(rb.position, PatrolStart.position) < 0.1)
                 {
                    sprite.flipX = false;
                    MoveDirection = Vector2.right;
                 }
                 if (Vector2.Distance(rb.position, PatrolEnd.position) < 0.1)
                 {
                    sprite.flipX = true; 
                    MoveDirection = Vector2.left;
                 
                 }
             }
            if (vertical)
            {
                if (Vector2.Distance(rb.position, PatrolStart.position) < 0.1)
                {
                    sprite.flipX = false;
                    MoveDirection = Vector2.down;
                }
                if (Vector2.Distance(rb.position, PatrolEnd.position) < 0.1)
                {
                    sprite.flipX = true;
                    MoveDirection = Vector2.up;

                }
            }
            if (diagonalUR)
            {
                if (Vector2.Distance(rb.position, PatrolStart.position) < 0.1)
                {
                    sprite.flipX = false;
                    MoveDirection = Vector2.down + Vector2.left;
                }
                if (Vector2.Distance(rb.position, PatrolEnd.position) < 0.1)
                {
                    sprite.flipX = true;
                    MoveDirection = Vector2.up + Vector2.right;

                }
            }
            rb.velocity = MoveDirection * PatrolSpeed;
        }
        if (!InPatrolRoute)
        {
            Vector3 direction = (PatrolCenter.position - transform.position).normalized;
            rb.velocity = direction * PatrolSpeed;
            if (Vector2.Distance(rb.position, PatrolCenter.position)< 0.1)
            {
                gameObject.transform.position = PatrolCenter.position;
                InPatrolRoute = true;
                if (horizontal)MoveDirection = Vector2.right;
                if (vertical)MoveDirection = Vector2.up;
                if (diagonalUR) MoveDirection = Vector2.right + Vector2.up;
                rb.velocity = MoveDirection * PatrolSpeed;
            }
            /*
            if (PatrolCenter.position == gameObject.transform.position)
            {
                InPatrolRoute = true;
                MoveDirection = Vector2.right;
                rb.velocity = MoveDirection * PatrolSpeed;
            }
            */
        }

    }
    private void Awake()
    {
        
    }

    // Start is called before the first frame update
    void Start()
    {
        animator = GetComponent<Animator>();
        sprite = gameObject.GetComponent<SpriteRenderer>();
        rb = GetComponent<Rigidbody2D>();
        if (horizontal)
        {
           MoveDirection = Vector2.right;
        }
        if (vertical)
        {
            MoveDirection = Vector2.up;
        }
        if (diagonalUR)
        {
            MoveDirection = Vector2.up + Vector2.right;
        }
        InPatrolRoute = true;
        if (combatInt == 1)
        {
            gameObject.SetActive(GameManager.Instance.combat1);
        }
        if (combatInt == 2)
        {
            gameObject.SetActive(GameManager.Instance.combat2);
        }
        if (combatInt == 4)
        {
            gameObject.SetActive(GameManager.Instance.combat4);
        }
        if (combatInt == 5)
        {
            gameObject.SetActive(GameManager.Instance.combat5);
        }
    }

    // Update is called once per frame
    void Update()
    {
        if(PlayerInRange) 
        {
            ChasePlayer();
        }
        if (!PlayerInRange)
        {
            Patrol();
        }
    }
}
